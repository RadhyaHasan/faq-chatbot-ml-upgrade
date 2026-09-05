# FAQ Chatbot v2 — Week 8 Capstone (Track C)

Upgrades the Week 7 FAQ Chatbot's matching engine from hand-coded word-overlap
rules to a real Data Science / ML technique: **TF-IDF + Cosine Similarity**.

## Files
- `knowledge_base.py` — 27 Q&A pairs (15 original + 12 new, shared by both engines)
- `engine_v1.py` — Week 7 baseline (word-overlap + stemming), reconstructed for a fair comparison
- `engine_v2.py` — Week 8 model (TF-IDF + Cosine Similarity, scikit-learn)
- `test_cases.py` — 20-question test set (10 original + 10 new, harder paraphrases)
- `compare.py` — runs both engines on the test set, tunes the v2 threshold, saves charts
- `chatbot_v2.py` — the runnable chatbot (CLI)
- `chatbot_v2.html` — browser version, no install needed (same engine, reimplemented in JS)
- `test_chatbot_v2.py` — automated test suite for v2
- `results.json`, `accuracy_comparison.png`, `confidence_scores.png` — real captured output

## Run it
```bash
pip install scikit-learn matplotlib
python3 chatbot_v2.py          # interactive chat (type 'demo' to run the test set, 'quit' to exit)
python3 test_chatbot_v2.py     # automated test suite
python3 compare.py             # full v1 vs v2 comparison + charts
```
Or just open `chatbot_v2.html` in any browser — no Python required.

## Result summary
- v1 (word-overlap): 15/20 on the test set
- v2 (TF-IDF + Cosine Similarity): 15/20 on the test set, plus a real per-answer confidence score
- Both share the same failure mode on fully-reworded questions with zero shared vocabulary — see the report for the full analysis.
