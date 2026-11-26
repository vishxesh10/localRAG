from pypdf import PdfReader


def read_pdf(pdf_path: str) -> str:
    """PDF se text extract karta hai"""
    reader = PdfReader(pdf_path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100) -> list[str]:
    """Bade text ko chhote chunks me todta hai"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
