# SE03 — AI Lab 10: BST Shape and Search Cost

## What this repository is about

This directory is the deliverable for AI Lab 10 of the SE-03 Algorithmic
Thinking course. It investigates how the insertion order of identical values
changes the shape, height, and search cost of a binary search tree by predicting
the outcome first, interrogating AI reasoning, and verifying every prediction
against a Python implementation.

## Repository contents

| File | Description |
|---|---|
| `bst_analysis.py` | Builds and measures all three BSTs |
| `my_predictions.md` | Predictions and post-code comparison |
| `prompts.md` | Exact prompts and their reasoning |

## Key findings

- **Sequence A (balanced order) height:** 3 node levels
- **Sequence B (ascending order) height:** 7 node levels
- **Sequence C (mixed order) height:** 7 node levels
- **In-order traversal of all three:** `[10, 25, 40, 50, 60, 75, 90]`
- **What insertion order does to search cost:** It can change worst-case
  successful search from three comparisons to all seven comparisons.

## Running the project

```bash
python3 bst_analysis.py
```

## AI tool used

OpenAI Codex was used as the prediction and verification partner.
