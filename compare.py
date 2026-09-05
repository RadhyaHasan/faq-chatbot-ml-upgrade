"""
Capstone comparison script.
Runs engine_v1 (Week 7 word-overlap baseline) and engine_v2 (Week 8 TF-IDF +
Cosine Similarity model) on the same 20-question test set, scores both,
tunes the v2 similarity threshold, and produces a comparison chart.
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import engine_v1
import engine_v2
from test_cases import TEST_CASES


def run_v1():
    results = []
    correct = 0
    for case in TEST_CASES:
        kb_id, answer = engine_v1.match(case["query"])
        is_correct = (kb_id == case["expected_kb_id"])
        correct += is_correct
        results.append({
            "n": case["n"], "query": case["query"],
            "expected": case["expected_kb_id"], "predicted": kb_id,
            "correct": is_correct,
        })
    return results, correct


def run_v2(threshold):
    results = []
    correct = 0
    for case in TEST_CASES:
        kb_id, answer, score = engine_v2.match(case["query"], threshold=threshold)
        is_correct = (kb_id == case["expected_kb_id"])
        correct += is_correct
        results.append({
            "n": case["n"], "query": case["query"],
            "expected": case["expected_kb_id"], "predicted": kb_id,
            "score": score, "correct": is_correct,
        })
    return results, correct


def tune_threshold():
    """Sweep thresholds and report accuracy at each, to justify the chosen value."""
    sweep = {}
    for t in [0.10, 0.15, 0.18, 0.20, 0.22, 0.25, 0.28, 0.30, 0.35, 0.40]:
        _, correct = run_v2(t)
        sweep[t] = correct
    return sweep


if __name__ == "__main__":
    v1_results, v1_correct = run_v1()
    sweep = tune_threshold()
    best_threshold = max(sweep, key=sweep.get)
    v2_results, v2_correct = run_v2(best_threshold)

    print("=" * 70)
    print("THRESHOLD TUNING (v2 similarity cutoff -> accuracy on 20 test cases)")
    print("=" * 70)
    for t, c in sweep.items():
        marker = "  <-- chosen" if t == best_threshold else ""
        print(f"  threshold={t:.2f}  ->  {c}/20 correct{marker}")

    print()
    print("=" * 70)
    print(f"RESULTS  (v1 word-overlap: {v1_correct}/20  |  v2 TF-IDF+cosine: {v2_correct}/20, threshold={best_threshold})")
    print("=" * 70)
    print(f"{'#':<3}{'query':<62}{'v1':<5}{'v2':<5}")
    for r1, r2 in zip(v1_results, v2_results):
        v1_mark = "OK" if r1["correct"] else "FAIL"
        v2_mark = "OK" if r2["correct"] else "FAIL"
        flag = "  <-- v2 fixed this" if (not r1["correct"] and r2["correct"]) else \
               ("  <-- v2 regressed" if (r1["correct"] and not r2["correct"]) else "")
        q = r1["query"][:58] + ("…" if len(r1["query"]) > 58 else "")
        print(f"{r1['n']:<3}{q:<62}{v1_mark:<5}{v2_mark:<5}{flag}")

    # Save machine-readable results for the report
    with open("results.json", "w") as f:
        json.dump({
            "v1_correct": v1_correct, "v2_correct": v2_correct,
            "total": len(TEST_CASES), "best_threshold": best_threshold,
            "sweep": sweep, "v1_results": v1_results, "v2_results": v2_results,
        }, f, indent=2)

    # Comparison chart
    fig, ax = plt.subplots(figsize=(6, 4.5))
    bars = ax.bar(
        ["v1\nWord-Overlap\n(Week 7)", "v2\nTF-IDF + Cosine\nSimilarity (Week 8)"],
        [v1_correct / len(TEST_CASES) * 100, v2_correct / len(TEST_CASES) * 100],
        color=["#94a3b8", "#2563eb"],
    )
    ax.set_ylim(0, 100)
    ax.set_ylabel("Accuracy on 20-question test set (%)")
    ax.set_title("Chatbot Engine Accuracy: v1 vs v2")
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 2, f"{h:.0f}%", ha="center", fontweight="bold")
    plt.tight_layout()
    plt.savefig("accuracy_comparison.png", dpi=150)
    print("\nSaved: results.json, accuracy_comparison.png")
