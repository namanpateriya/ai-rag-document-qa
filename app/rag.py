import faiss
import numpy as np
from app.embeddings import embed_texts

class VectorStore:

    def __init__(self):
        self.index = None
        self.texts = []

    def build(self, chunks):
        embeddings = embed_texts(chunks)

        dimension = len(embeddings[0])
        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(np.array(embeddings))
        self.texts = chunks

    def search(self, query, top_k=3):
        query_vec = embed_texts([query])
        distances, indices = self.index.search(query_vec, top_k)

        results = [self.texts[i] for i in indices[0]]
        return results
