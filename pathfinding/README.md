# SE03 — AI Lab 12: Greedy vs Dijkstra's

## What this repository is about

This directory is the deliverable for AI Lab 12 of the SE-03 Algorithmic
Thinking course. It builds a weighted graph that traps a naive greedy
shortest-path strategy, proves greedy returns a sub-optimal route, and
implements Dijkstra's algorithm to find the true shortest path, with a
documented explanation of exactly why greedy fails here.

## Repository contents

| File | Description |
|---|---|
| `dijkstra.py` | Dijkstra's algorithm using `heapq`, with path reconstruction |
| `my_analysis.md` | Hand predictions, results table, and greedy-failure analysis |
| `prompts.md` | Exact prompts used and the reasoning behind each one |

## Key findings

- **Naive greedy path and cost (A -> D):** A -> B -> D, cost 11
- **Dijkstra's shortest path and cost (A -> D):** A -> C -> D, cost 8
- **Why greedy fails here:** The cheapest immediate edge commits the route to
  a later edge whose cost makes the full path more expensive.
- **The rule I now apply before trusting greedy:** Prove the greedy-choice
  property or find a counterexample before accepting a local rule.

## Running the project

```bash
python3 dijkstra.py
```

## AI tool used

OpenAI Codex was used as the analysis and implementation partner.
