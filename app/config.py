import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = str(BASE_DIR / "db")
DEFAULT_PDF = str(BASE_DIR / "lecture.pdf")

# Google Gemini Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
LLM_MODEL = "gemini-2.5-flash-lite"
COLLECTION_NAME = "instant_rag_notes"
