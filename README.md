# AI RAG Document QA

Answer questions from documents using Retrieval-Augmented Generation (RAG).

Supports:

* CLI-based document QA
* API-based document QA

---

## Features

* Document ingestion and chunking
* Embeddings using sentence-transformers
* Vector search using FAISS
* Multi-model support (OpenAI, Anthropic, Gemini)
* Context-grounded answers
* CLI and API support
* Evaluation support

---

## Setup

```bash
git clone <repo_url>
cd ai-rag-document-qa
pip install -r requirements.txt
```

Create `.env` file:

```
PROVIDER=openai
MODEL=gpt-4o-mini

OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
GEMINI_API_KEY=your_key
```

---

## Execution Modes

### CLI

```bash
python -m app.cli --file data/sample.txt
python -m app.cli --query "What is AI?"
```

---

### API

```bash
uvicorn app.main:app --reload
```

Endpoints:

POST /upload
GET /query?q=your_query

---

## CLI Options

| Option  | Description   |
| ------- | ------------- |
| --file  | Load document |
| --query | Ask question  |

---

## Use Cases

* Knowledge assistants
* Document search systems
* Enterprise Q&A tools
* Policy and compliance bots
* Research assistants

---

## Roadmap

* Add persistent vector store
* Add hybrid search
* Improve chunking strategies
* Add UI
* Add answer scoring

---

Built for real-world AI system design
