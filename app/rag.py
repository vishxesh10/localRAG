from google import genai
from app.config import DEFAULT_PDF, GEMINI_API_KEY
from app.database import get_collection
from app.document import read_pdf, chunk_text


def get_gemini_client():
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set. Please set GEMINI_API_KEY in your .env file.")
    return genai.Client(api_key=GEMINI_API_KEY)


def build_knowledge_base(pdf_path: str = DEFAULT_PDF) -> int:
    """Reads PDF and stores chunks into ChromaDB vector database."""
    text = read_pdf(pdf_path)
    chunks = chunk_text(text)

    collection = get_collection()
    collection.add(
        documents=chunks,
        ids=[f"chunk-{i}" for i in range(len(chunks))],
    )
    return len(chunks)


def answer_question(question: str) -> str:
    """Retrieves relevant context from ChromaDB and generates answer using Google Gemini."""
    collection = get_collection()
    results = collection.query(query_texts=[question], n_results=3)

    if not results["documents"] or not results["documents"][0]:
        return "No relevant information found in the knowledge base."

    context = "\n\n".join(results["documents"][0])

    prompt = f"""Use ONLY the context below to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question: {question}

Answer:"""

    client = get_gemini_client()
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )
    return response.text
