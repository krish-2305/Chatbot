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

## 📂 Project Structure
Bot/
│
├── chatbot-rag/
│   ├── api.py          # FastAPI backend (API endpoints)
│   ├── chatbot.py      # Core chatbot logic (parse, store, ask)
│   ├── app.py          # Streamlit frontend UI
│   ├── main.py         # Entry point (run services together)
│
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
├── .gitignore          # Ignore venv, .env, __pycache__, etc.
└── README.md           # Project documentation
