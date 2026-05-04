from evaluation.evaluator import evaluate


def optimize():
    results = evaluate()

    failures = [r for r in results if r["error"]]

    print("\nFailures:", len(failures))

    if failures:
        print("Investigate retrieval or model issues")
    else:
        print("System stable")


if __name__ == "__main__":
    optimize()
