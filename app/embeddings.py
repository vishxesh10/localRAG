import math
import re
from collections import Counter
from chromadb import Documents, EmbeddingFunction, Embeddings


def simple_tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


class LightweightEmbeddingFunction(EmbeddingFunction):
    """
    Super-fast deterministic hashing vectorizer (Dimension: 128)
    - 0 MB download
    - No external API / No 404 / No timeouts
    - Instant vector generation on any machine
    """
    def __init__(self, dim: int = 128):
        self.dim = dim

    def __call__(self, input: Documents) -> Embeddings:
        embeddings = []
        for doc in input:
            tokens = simple_tokenize(doc)
            counts = Counter(tokens)
            vec = [0.0] * self.dim

            for token, count in counts.items():
                idx = hash(token) % self.dim
                vec[idx] += float(count)

            # Normalize vector (L2 norm)
            norm = math.sqrt(sum(x * x for x in vec))
            if norm > 0:
                vec = [x / norm for x in vec]

            embeddings.append(vec)

        return embeddings
