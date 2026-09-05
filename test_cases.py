"""
Test set for the capstone comparison: 20 real test cases.
- Q1-Q10: the exact 10 questions from the Week 7 report (kept for continuity).
- Q11-Q20: 10 new questions written for the capstone, deliberately reworded
  (not copy-pasted from the knowledge base) and covering the 12 new KB
  entries added this week, to stress-test generalization.

expected_kb_id = None means "should be refused" (out of scope).
"""

TEST_CASES = [
    {"n": 1, "query": "What's the real difference between compiling code and interpreting it?", "expected_kb_id": 1},
    {"n": 2, "query": "Why do developers bother with Git instead of just saving files manually?", "expected_kb_id": 2},
    {"n": 3, "query": "I keep hearing 'frontend' and 'backend' - what do they mean?", "expected_kb_id": 3},
    {"n": 4, "query": "Can you explain what an API does, simply?", "expected_kb_id": 4},
    {"n": 5, "query": "Is a linked list basically the same as an array?", "expected_kb_id": 5},
    {"n": 6, "query": "Can you write the full code for a to-do list app in Python?", "expected_kb_id": None},
    {"n": 7, "query": "What's a good career path after graduating in CS?", "expected_kb_id": None},
    {"n": 8, "query": "What's your opinion on the best pizza toppings?", "expected_kb_id": None},
    {"n": 9, "query": "Can you help me debug this 200-line error log I'm pasting?", "expected_kb_id": None},
    {"n": 10, "query": "What is quantum computing used for?", "expected_kb_id": None},
    {"n": 11, "query": "How does a stack differ from a queue when removing items?", "expected_kb_id": 17},
    {"n": 12, "query": "Why would I use JSON instead of plain text to send data between a client and a server?", "expected_kb_id": 22},
    {"n": 13, "query": "What's the benefit of catching errors instead of letting the program crash?", "expected_kb_id": 25},
    {"n": 14, "query": "If two tables are related, how does one row point to a matching row in another table?", "expected_kb_id": 26},
    {"n": 15, "query": "What happens when you combine two separate lines of development back together?", "expected_kb_id": 27},
    {"n": 16, "query": "Why is renting server space online better than buying my own hardware?", "expected_kb_id": 23},
    {"n": 17, "query": "Can you recommend a laptop for computer science students?", "expected_kb_id": None},
    {"n": 18, "query": "What's a good gift idea for a programmer friend?", "expected_kb_id": None},
    {"n": 19, "query": "Can you write me a full essay about the history of computers?", "expected_kb_id": None},
    {"n": 20, "query": "What's the weather like today?", "expected_kb_id": None},
]
