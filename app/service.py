from app.chunking import chunk_text
from app.rag import VectorStore
from app.utils.model import ModelClient
from app.utils.logger import get_logger

logger = get_logger(__name__)
model = ModelClient()

store = VectorStore()


def load_document(text):
    chunks = chunk_text(text)
    store.build(chunks)
    return len(chunks)


def answer_query(query):
    context_chunks = store.search(query)

    context = "\n\n".join(context_chunks)

    prompt = f"""
Answer the question based ONLY on the context below.

Context:
{context}

Question:
{query}
"""

    return model.generate(prompt)
