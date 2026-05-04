def chunk_text(text, chunk_size=300, overlap=50):
    text = text.replace("\n", " ").strip()

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
