# SE03 — AI Lab 09: Interrogating Search Strategy Reasoning

## What this repository is about

This directory is the deliverable for AI Lab 9 of the SE-03 Algorithmic
Thinking course. Three search strategies—linear, binary, and hash set—were
compared on an unsorted dataset of 50,000 product IDs. AI was asked to
recommend a strategy with no guidance, then challenged on its unstated
assumptions through two adversarial scenarios. All three strategies were
benchmarked and compared against theoretical predictions.

## Repository contents

| File | Description |
|---|---|
| `products.py` | Seeded catalogue and four search targets |
| `search_strategies.py` | Linear, cached binary, and cached hash search |
| `benchmark.py` | Setup and 1,000-run search timings |
| `analysis.md` | Reasoning, challenges, results, and reflection |

## Key findings

### Strategy comparison

| Approach | Setup | Per-search | Best for |
|---|---|---|---|
| Linear search | O(1) | O(n) | A few queries or constrained memory |
| Sort + binary | O(n log n) | O(log n) | Ordered and range operations |
| Hash set | O(n) | O(1) average | Repeated exact membership queries |

### AI's initial recommendation

AI recommended a hash set, which was correct for this static catalogue and
4,000 measured membership queries but depended on memory and update assumptions.

### Most surprising benchmark result

Binary search beat linear even for the target at index 100: C-backed bisect
took about 0.24 µs versus 0.84 µs for 101 Python-level linear comparisons.

### Final recommendation for this specific problem

Build and reuse a hash set. Its 0.00074380-second setup was quickly amortised,
and its 0.00101176-second total was the fastest measured result.

## Running the benchmark

```bash
python3 benchmark.py
```

## AI tool used

OpenAI Codex was used as the recommendation and interrogation partner.
