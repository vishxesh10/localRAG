from fastapi import APIRouter, UploadFile, File
import shutil
from pathlib import Path
from app.rag import answer_question, build_knowledge_base

router = APIRouter()

# Uploads folder
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.get("/")
def home():
    return {"status": "Server chal raha hai!"}


@router.get("/ask")
def ask(question: str = "What is RAG?"):
    """Sawal puchne ke liye endpoint"""
    ans = answer_question(question)
    return {"question": question, "answer": ans}


@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    """PDF file receive karke read aur index karta hai"""
    file_path = UPLOAD_DIR / file.filename

    # File ko save karo
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # PDF se database build karo
    total_chunks = build_knowledge_base(str(file_path))

    return {
        "message": f"{file.filename} uploaded and processed ({total_chunks} chunks)!",
        "filename": file.filename,
    }
