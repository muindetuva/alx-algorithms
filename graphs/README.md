# SE03 — AI Lab 11: Tracing BFS and DFS

## What this repository is about

This directory is the deliverable for AI Lab 11 of the SE-03 Algorithmic
Thinking course. It traces breadth-first and depth-first search on one directed
graph by hand, through an AI tool, and against a Python implementation to show
why a queue and a recursion stack produce different orders on identical input.

## Repository contents

| File | Description |
|---|---|
| `traversals.py` | Graph, BFS, DFS, and internal-state snapshots |
| `my_traces.md` | Hand traces and post-code comparison |
| `prompts.md` | Exact prompts and their reasoning |

## Key findings

- **BFS order from A:** A → B → C → D → E → F
- **DFS order from A:** A → B → D → E → F → C
- **Why F is reached differently:** BFS discovers F from C at the next level;
  DFS reaches it from E while completing B's subtree.
- **Why queue vs stack changes the order:** FIFO explores by distance, while
  LIFO recursion completes one path before its siblings.

## Running the project

```bash
python3 traversals.py
```

## AI tool used

OpenAI Codex was used as the tracing and verification partner.
