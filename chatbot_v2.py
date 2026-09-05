"""
FAQ Chatbot for CS Fundamentals - v2 (Week 8 Capstone)
Same scope and rules as the Week 7 chatbot, now answered by a real
Data Science / ML technique (TF-IDF + Cosine Similarity) instead of a
hand-coded word-overlap rule.

Run: python3 chatbot_v2.py
"""

import engine_v2

REFUSAL = "That's outside what I can help with here - I can only answer core CS/programming fundamentals questions."

BANNER = """FAQ Chatbot for CS Fundamentals v2 (TF-IDF + Cosine Similarity engine)
Ask a beginner CS question (Git, APIs, OOP, arrays vs linked lists, stacks, etc.)
Anything outside that scope gets politely refused. Type 'quit' to exit, 'demo' to run the test set.
"""


def answer(query: str) -> str:
    kb_id, result, score = engine_v2.match(query)
    if kb_id is None:
        return REFUSAL
    return result


def run_demo():
    from test_cases import TEST_CASES
    correct = 0
    for case in TEST_CASES:
        kb_id, result, score = engine_v2.match(case["query"])
        ok = (kb_id == case["expected_kb_id"])
        correct += ok
        tag = "PASS" if ok else "FAIL"
        print(f"[{tag}] (score={score}) Q{case['n']}: {case['query']}")
    print(f"\n{correct}/{len(TEST_CASES)} tests passed.")


if __name__ == "__main__":
    print(BANNER)
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            break
        if user_input.lower() == "demo":
            run_demo()
            continue
        print(f"Bot: {answer(user_input)}\n")
