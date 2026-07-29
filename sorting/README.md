# SE03 — AI Lab 06: Sorting Algorithm Benchmark

## What this repository is about

This directory is the deliverable for AI Lab 6 of the SE-03 Algorithmic
Thinking course. Five sorting algorithms—Bubble, Insertion, Merge, randomized
Quicksort, and Python's Timsort—were benchmarked across five datasets with
deliberately chosen properties. Predictions were made independently before
running the benchmark, then compared against AI reasoning and empirical
results.

## Repository contents

| File | Description |
|---|---|
| `sorting.py` | Four non-mutating custom sorting implementations |
| `benchmark.py` | Five datasets and timing for all five algorithms |
| `predictions.md` | Predictions, results, comparison, and reflection |

## Key findings

### Most interesting result

Early-exit Bubble ranked second on already sorted input but last on every other
dataset, showing how strongly one optimization and input shape can matter.

### Where AI predictions were wrong

AI overestimated Insertion's advantage on nearly sorted data: randomized
Quicksort finished in 0.008166 seconds versus Insertion's 0.037608 seconds.

### Algorithm recommendation by use case

| Use case | Recommended algorithm | Reason |
|---|---|---|
| Large random dataset | Timsort | Fast optimized O(n log n) implementation |
| Already-sorted data | Timsort | Detects the existing run in linear time |
| Nearly-sorted data | Timsort | Exploits natural runs and local order |
| Memory-constrained system | Insertion | In-place with O(1) auxiliary space |
| Production Python code | Timsort | Built into `sorted()` and `list.sort()` |

## Running the benchmark

```bash
python3 benchmark.py
```

All datasets contain 10,000 elements. Bubble and Insertion run once per
dataset; the three faster approaches report the median of three runs.

## AI tool used

OpenAI Codex was used as the prediction and implementation partner.
