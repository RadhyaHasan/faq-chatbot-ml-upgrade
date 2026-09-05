"""
Engine v1 - the Week 7 baseline.
Word-overlap matching with light stemming (first 5 letters) and a
"at least 2 shared key words" rule, exactly as documented in the
Week 7 report (Section 7, Bug 1 and Bug 2 fixes).
"""

from knowledge_base import KNOWLEDGE_BASE

STOPWORDS = {
    "what", "is", "a", "an", "the", "of", "and", "or", "to", "in", "on",
    "for", "do", "does", "you", "your", "i", "me", "can", "explain",
    "basically", "same", "real", "difference", "between", "it", "just",
    "keep", "hearing", "mean", "simply", "bother", "instead", "manually",
    "files", "saving", "developers", "why", "how", "opinion", "help",
    "with", "this", "im", "pasting", "used", "good", "after",
}


def _stem(word: str) -> str:
    return word[:5]


def _keywords(text: str):
    words = [w.strip(".,?!'\"").lower() for w in text.split()]
    return {_stem(w) for w in words if w and w not in STOPWORDS and len(w) > 2}


def match(query: str):
    """Return (kb_id, answer) if matched, or (None, refusal_reason)."""
    query_kw = _keywords(query)
    if not query_kw:
        return None, "empty query"

    best_id, best_overlap = None, 0
    for entry in KNOWLEDGE_BASE:
        kb_kw = _keywords(entry["question"])
        shared = query_kw & kb_kw
        required = 2 if len(kb_kw) > 1 else len(kb_kw)
        if len(shared) >= required and len(shared) > best_overlap:
            best_overlap = len(shared)
            best_id = entry["id"]

    if best_id is None:
        return None, "no match above threshold"

    answer = next(e["answer"] for e in KNOWLEDGE_BASE if e["id"] == best_id)
    return best_id, answer
