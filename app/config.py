from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = str(BASE_DIR / "db")
DEFAULT_PDF = str(BASE_DIR / "lecture.pdf")

# Model settings
EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2"
OLLAMA_URL = "http://localhost:11434/api/embeddings"
COLLECTION_NAME = "my_notes"
