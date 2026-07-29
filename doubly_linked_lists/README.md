# SE03 — AI Lab 03: Browser History with a Doubly Linked List

## What this repository is about

This directory is the deliverable for AI Lab 3 of the SE-03 Algorithmic
Thinking course. A browser back/forward history feature was designed and
implemented using a doubly linked list. AI was used as a design partner at
the reasoning stage to evaluate structure choices and trace pointer behaviour
through concrete examples before implementation.

## Repository contents

| File | Description |
|---|---|
| `browser_history.py` | `BrowserHistory` class implementation |
| `test_browser_history.py` | Full test suite covering edge cases |
| `design_notes.md` | Design reasoning before and after AI collaboration |

## Design decision

- **Structure chosen:** Doubly Linked List
- **Why not a Python list:** Removing every forward entry from a list takes
  time proportional to the number removed, while a DLL discards that branch
  with constant-time pointer updates.
- **The key insight:** A new visit links a node after `current`, makes that
  node the new `tail`, and leaves the former forward chain detached.

## Complexity

| Operation | Complexity |
|---|---|
| `visit(url)` | O(1) |
| `back()` | O(1) |
| `forward()` | O(1) |
| `get_current()` | O(1) |
| `get_history()` | O(n) |

## Running the project

```bash
python3 browser_history.py
python3 test_browser_history.py
```

## AI tool used

OpenAI Codex was used as the design and implementation partner.
