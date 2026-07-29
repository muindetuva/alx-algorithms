# SE03 — AI Lab 07: Tracing Repeated Work in Naive Recursion

## What this repository is about

This directory is the deliverable for AI Lab 7 of the SE-03 Algorithmic
Thinking course. A naive recursive solution to the minimum coin change problem
was implemented, its call tree was traced manually, and AI was used to explain
where repeated work occurs and why the naive approach is exponential. The lab
documents both the problem and a preview of the fix without implementing
memoisation.

## Repository contents

| File | Description |
|---|---|
| `coin_change.py` | Naive recursion, call counter, and benchmark |
| `analysis.md` | Observations, manual trace, comparison, and fix preview |

## Key findings

### Call count growth

| amount | calls made |
|---:|---:|
| 10 | 101 |
| 20 | 2,221 |
| 30 | 47,325 |
| 40 | 1,010,369 |

### The overlapping subproblem

Small remaining amounts such as `coin_change(1)` and `coin_change(0)` are
recomputed along many different coin-choice paths.

### Time complexity of naive solution

The recursion is exponential—loosely O(c^(A/s)) for c coin types, amount A,
and smallest coin s—because each uncached positive amount branches by coin.

### Number of unique subproblems

There are only A + 1 meaningful nonnegative remaining amounts from 0 through
A. Memoisation would solve each once, giving O(A × c) time, or O(A) for a fixed
four-coin set.

## Running the project

```bash
python3 coin_change.py
```

## AI tool used

OpenAI Codex was used to analyse and verify the repeated work.
