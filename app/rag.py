import faiss
import numpy as np
import os
from app.embeddings import embed_texts

class VectorStore:

    def __init__(self):
        self.index = None
        self.texts = []

    def build(self, chunks):
        embeddings = embed_texts(chunks)

        embeddings = np.array(embeddings).astype("float32")

        dimension = len(embeddings[0])
        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)
        self.texts = chunks

    def search(self, query, top_k=None):
        if self.index is None:
            return []

        if top_k is None:
            top_k = int(os.getenv("TOP_K", 3))

        query_vec = np.array(embed_texts([query])).astype("float32")

        distances, indices = self.index.search(query_vec, top_k)

        results = [self.texts[i] for i in indices[0] if i < len(self.texts)]
        return results
