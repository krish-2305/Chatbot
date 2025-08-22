# 🤖 Chatbot RAG (FastAPI + Streamlit)

A simple **RAG-based chatbot** built with **FastAPI** as the backend and **Streamlit** as the frontend.  
Users can upload **PDF documents** and ask questions, and the chatbot will retrieve answers from the uploaded content.

---

## 🚀 Features
- 📂 Upload multiple **PDF file**  
- 🔎 Ask natural language questions about the documents  
- ⚡ Backend: **FastAPI** (API endpoints)  
- 🎨 Frontend: **Streamlit** (interactive UI)  
- 🔒 Secrets managed in `.env`  

---

# 📂 Bot Project

* [README.md](./README.md)
* [.env.example](./.env.example)
* [.gitignore](./.gitignore)
* [requirements.txt](./requirements.txt)
* [chatbot-rag](./chatbot-rag)
  * [api.py](./chatbot-rag/api.py) – FastAPI backend (API endpoints)
  * [chatbot.py](./chatbot-rag/chatbot.py) – Core chatbot logic (parse, store, ask)
  * [app.py](./chatbot-rag/app.py) – Streamlit frontend UI
  * [main.py](./chatbot-rag/main.py) – Entry point (run services together)


## Requirements
- Python 3.8 or higher
- Virtual environment (recommended)
- Dependencies listed in `requirements.txt`
