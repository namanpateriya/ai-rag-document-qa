# Evaluation

Evaluate the RAG-based document question-answering system.

---

## Setup

Ensure environment variables are configured and dependencies installed.

---

## How to Run Evaluator

```bash
python -m evaluation.evaluator
```

---

## How to Run Optimizer

```bash
python -m evaluation.optimizer
```

---

## Input Required

Test cases are defined in:

evaluation/test_cases.json

Each test case includes:

* document text
* query

---

## Sample Output

Query: What is AI?
Answer: Artificial Intelligence is the simulation of human intelligence...

---

## Evaluation Summary

The evaluator checks:

* whether system returns errors
* whether answer length is sufficient

---

## Notes

* This evaluates pipeline reliability, not semantic correctness
* Extend with LLM judge for deeper validation

---

Built to validate RAG pipeline performance
