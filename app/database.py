import chromadb
from app.config import DB_PATH, COLLECTION_NAME
from app.embeddings import LightweightEmbeddingFunction


def get_collection():
    """Connects to the persistent ChromaDB collection."""
    client = chromadb.PersistentClient(path=DB_PATH)
    ef = LightweightEmbeddingFunction(dim=128)

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=ef,
    )
