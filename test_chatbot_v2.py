"""
Automated test suite for chatbot v2.
Same style as Week 7's test_chatbot.py: runs every case in test_cases.py
against engine_v2 and reports PASS/FAIL per question plus a final score.
Run: python3 test_chatbot_v2.py
"""

import engine_v2
from test_cases import TEST_CASES


def run():
    passed = 0
    for case in TEST_CASES:
        kb_id, answer, score = engine_v2.match(case["query"])
        ok = (kb_id == case["expected_kb_id"])
        passed += ok
        tag = "PASS" if ok else "FAIL"
        expected_desc = f"KB#{case['expected_kb_id']}" if case["expected_kb_id"] else "REFUSE"
        got_desc = f"KB#{kb_id}" if kb_id else "REFUSE"
        print(f"[{tag}] Q{case['n']} (expected {expected_desc}, got {got_desc}, score={score}): {case['query']}")
    print(f"\n{passed}/{len(TEST_CASES)} tests passed.")
    return passed, len(TEST_CASES)


if __name__ == "__main__":
    run()
