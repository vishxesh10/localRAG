from fastapi import APIRouter, UploadFile, File
import shutil
from pathlib import Path
from app.rag import answer_question, build_knowledge_base

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.get("/")
def home():
    return {"status": "Server is running"}


@router.get("/ask")
def ask(question: str = "What is RAG?"):
    """Endpoint to answer questions from the knowledge base."""
    ans = answer_question(question)
    return {"question": question, "answer": ans}


@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    """Receives, saves, and indexes an uploaded PDF document."""
    file_path = UPLOAD_DIR / file.filename

    # Save uploaded file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process and index document
    total_chunks = build_knowledge_base(str(file_path))

    return {
        "message": f"{file.filename} uploaded and processed ({total_chunks} chunks).",
        "filename": file.filename,
    }
