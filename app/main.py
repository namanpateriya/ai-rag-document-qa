from fastapi import FastAPI, UploadFile, File
from app.service import load_document, answer_query

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    text = (await file.read()).decode("utf-8")
    chunks = load_document(text)
    return {"chunks": chunks}

@app.get("/query")
def query(q: str):
    answer = answer_query(q)
    return {"answer": answer}
