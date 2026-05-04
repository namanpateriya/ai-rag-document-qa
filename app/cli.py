import argparse
from app.service import load_document, answer_query

parser = argparse.ArgumentParser()

parser.add_argument("--file", help="Path to text file")
parser.add_argument("--query", help="Query to ask")

args = parser.parse_args()

if args.file:
    with open(args.file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = load_document(text)
    print(f"Loaded document with {chunks} chunks")

if args.query:
    answer = answer_query(args.query)
    print("\nAnswer:\n", answer)
