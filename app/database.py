import chromadb
from chromadb.utils import embedding_functions
from app.config import DB_PATH, COLLECTION_NAME, EMBEDDING_MODEL, OLLAMA_URL


def get_collection():
    """ChromaDB collection connect karne ke liye"""
    client = chromadb.PersistentClient(path=DB_PATH)
    ef = embedding_functions.OllamaEmbeddingFunction(
        url=OLLAMA_URL,
        model_name=EMBEDDING_MODEL,
    )
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=ef,
    )
