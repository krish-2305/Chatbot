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
│ ├── api.py # FastAPI backend
│ ├── chatbot.py # Helper functions (parse/store/ask)
│ ├── app.py # Streamlit frontend
│ ├── main.py
├── requirements.txt # Python dependencies
├── .env.example # Example environment variables
├── .gitignore
└── README.md
