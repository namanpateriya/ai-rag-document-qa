import json
import os
from app.service import load_document, answer_query

BASE = os.path.dirname(__file__)
TEST_FILE = os.path.join(BASE, "test_cases.json")


def evaluate():
    with open(TEST_FILE) as f:
        cases = json.load(f)

    results = []

    for case in cases:
        load_document(case["document"])

        answer = answer_query(case["query"])

        is_error = str(answer).lower().startswith("error")
        length_ok = len(answer) > 10

        results.append({
            "query": case["query"],
            "error": is_error,
            "length_ok": length_ok
        })

        print("\nQuery:", case["query"])
        print("Answer:", answer)

    return results


def summarize(results):
    total = len(results)
    errors = sum(1 for r in results if r["error"])
    valid = sum(1 for r in results if r["length_ok"])

    print("\n=== SUMMARY ===")
    print(f"Total: {total}")
    print(f"Errors: {errors}")
    print(f"Valid answers: {valid}")


if __name__ == "__main__":
    res = evaluate()
    summarize(res)
