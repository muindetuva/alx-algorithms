# SE03 — AI Lab 08: Longest Increasing Subsequence — DP

## What this repository is about

This directory is the deliverable for AI Lab 8 of the SE-03 Algorithmic
Thinking course. The Longest Increasing Subsequence problem was solved using
both dynamic programming approaches—memoisation and tabulation. The lab
documents the DP recognition process, both implementations, a structured
comparison, and an edge-case analysis.

## Repository contents

| File | Description |
|---|---|
| `lis.py` | Memoised and tabulated LIS with a shared test suite |
| `analysis.md` | Recognition, recurrence, reviews, and comparison |

## Problem

Given a list of integers, find the length of the longest strictly increasing
subsequence.

## Complexity

| Approach | Time | Space |
|---|---|---|
| Memoised | O(n²) | O(n) cache plus O(n) recursion stack |
| Tabulated | O(n²) | O(n) DP array |

## Key findings

- **Recurrence:** `LIS(i) = max(LIS(j) + 1)` for all `j < i` where
  `nums[j] < nums[i]`, defaulting to 1.
- **Preferred approach:** Tabulation avoids recursion-depth risk and has lower
  constant overhead for the full LIS problem.
- **Edge case handled:** All-equal input returns 1.

## Running the project

```bash
python3 lis.py
```

## AI tool used

OpenAI Codex was used as the step-by-step DP collaborator.
