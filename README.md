# Local RAG Backend API 📚🤖

A fast, lightweight, and modular **Retrieval-Augmented Generation (RAG)** backend built with **FastAPI**, **ChromaDB**, and **Ollama**. It allows users to upload documents (PDFs), index them into a local vector database, and ask context-aware questions with AI.

---

## 🚀 Features

- **Document Ingestion:** Upload `.pdf` documents directly via REST API.
- **Text Chunking & Preprocessing:** Automatic text extraction and chunking with configurable overlap.
- **Local Vector Database:** Powered by **ChromaDB** with persistence on disk.
- **Local AI Inference:** 
  - Embeddings: `nomic-embed-text`
  - Generation: `llama3.2` (via Ollama)
- **FastAPI Endpoints:** Clean endpoints for uploading, re-indexing, and querying with Swagger documentation (`/docs`).
- **CORS Enabled:** Ready to connect with modern frontends (React, Vite, Next.js, Electron).

---

## 📁 Project Structure

```
localRAG-backend/
│
├── app/
│   ├── config.py         # Paths, model names, and ChromaDB configuration
│   ├── database.py       # ChromaDB client & collection helper
│   ├── document.py       # PDF parsing & text chunking logic
│   ├── rag.py            # Embedding generation, vector search, & LLM prompt logic
│   └── routes.py         # API route handlers (/upload, /ask, /build)
│
├── main.py               # FastAPI application entry point with CORS
├── pyproject.toml        # Dependencies and project specifications
└── README.md             # Project documentation
```

---

## 🛠️ Prerequisites

1. **Python:** >= 3.10
2. **Ollama:** Installed and running locally ([Download Ollama](https://ollama.com/download))
   Pull the required models:
   ```bash
   ollama pull nomic-embed-text
   ollama pull llama3.2
   ```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vishxesh10/localRAG.git
   cd localRAG
   ```

2. **Set up virtual environment & install dependencies:**
   Using `uv` (recommended):
   ```bash
   uv venv
   uv pip install -r pyproject.toml
   ```
   Or using standard `pip`:
   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   pip install -r pyproject.toml
   ```

3. **Start the FastAPI Server:**
   ```bash
   uv run uvicorn main:app --reload
   ```

The server will start at `http://127.0.0.1:8000`.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health check endpoint. |
| `POST` | `/upload` | Upload a PDF document, chunk it, and index it into ChromaDB. |
| `GET` | `/ask?question=...` | Query the knowledge base and receive an LLM-generated answer. |
| `GET` | `/build` | Re-index the default document (`lecture.pdf`). |

Interactive Swagger API docs available at:  
👉 **`http://127.0.0.1:8000/docs`**

---

## 🔒 Privacy & Offline Capability

All embeddings and LLM generations run **100% locally** on your machine. No data or queries leave your local environment.
