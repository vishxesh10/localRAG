import ollama
from app.config import LLM_MODEL, DEFAULT_PDF
from app.database import get_collection
from app.document import read_pdf, chunk_text


def build_knowledge_base(pdf_path: str = DEFAULT_PDF) -> int:
    """PDF ko read karke database me chunks store karta hai"""
    text = read_pdf(pdf_path)
    chunks = chunk_text(text)

    collection = get_collection()
    collection.add(
        documents=chunks,
        ids=[f"chunk-{i}" for i in range(len(chunks))],
    )
    return len(chunks)


def answer_question(question: str) -> str:
    """Question ka context dhoondh kar LLM se answer leta hai"""
    collection = get_collection()
    results = collection.query(query_texts=[question], n_results=3)

    if not results["documents"] or not results["documents"][0]:
        return "Database me koi relevant information nahi mili."

    context = "\n\n".join(results["documents"][0])

    prompt = f"""Use ONLY the context below to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question: {question}

Answer:"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]
