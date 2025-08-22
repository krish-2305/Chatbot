"""this module contains the logic for chatbot using Gemini API"""

from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_core.documents.base import Document
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import os
from langchain_community.document_loaders.blob_loaders import Blob
import logging
from langchain_community.document_loaders.parsers import PyPDFParser

# setup logger object for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# load environment variables
load_dotenv(find_dotenv())
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    logger.error("GEMINI_API_KEY is not set")
    raise ValueError("GEMINI_API_KEY is not set")

# create Gemini instances
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=GEMINI_API_KEY)

# setup Chroma database to store the documents
chroma = Chroma(
    collection_name="documents",
    collection_metadata={"name": "documents", "description": "store documents"},
    persist_directory="./data",
    embedding_function=embeddings,
)

# create a retriever to search the document
retriever = chroma.as_retriever(search_kwargs={"k": 2})

# create a prompt template
TEMPLATE = """
Here is the context:

<context>
{context}
</context>

And here is the question that must be answered using that context:

<question>
{input}
</question>

Please read through the provided context carefully. Then, analyze the question and attempt to find a
direct answer to the question within the context.

If you are able to find a direct answer, provide it and elaborate on relevant points from the
context using bullet points "-".

If you cannot find a direct answer based on the provided context, outline the most relevant points
that give hints to the answer of the question. For example:

If no answer or relevant points can be found, or the question is not related to the context, simply
state the following sentence without any additional text:

i couldnt find an answer did not find an answer to your question.

Output your response in plain text without using the tags <answer> and </answer> and ensure you are not
quoting context text in your response since it must not be part of the answer.
"""

PROMPT = ChatPromptTemplate.from_template(TEMPLATE)

# create the document parsing chain to inject the document into the chatbot
llm_chain = create_stuff_documents_chain(llm, PROMPT)

# create the retrieval chain
retrieval_chain = create_retrieval_chain(retriever, llm_chain)

# create function to store the document into the database
def store_document(documents: list[Document]) -> str:
    """store the document into the database
    Args:
        documents (list[dict]): list of documents to store
    """
    chroma.add_documents(documents=documents)
    return "document stored successfully"

# create a function to retrieve the document from the database
def retrieve_document(query: str) -> list[Document]:
    """retrieve the document from the database
    Args:
        query (str): query to search the document
    """
    documents = retriever.invoke(input=query)
    return documents

def ask_question(query: str) -> str:
    """chat with the chatbot
    Args:
        query (str): query to ask the chatbot
    """
    response = retrieval_chain.invoke({"input": query})
    answer = response["answer"]
    return answer

# create a pdf parser
parser = PyPDFParser()

def parse_pdf(file_content: bytes) -> list[Document]:
    """parse the pdf file
    Args:
        file_content (bytes): content of the pdf file
    """
    blob = Blob(data=file_content)
    document = [doc for doc in parser.lazy_parse(blob)]
    return document