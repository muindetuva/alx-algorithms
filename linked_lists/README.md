# SE03 — AI Lab 02: Bug Hunt

## What this repository is about

This directory is the deliverable for AI Lab 2 of the SE-03 Algorithmic Thinking course. An AI tool was asked to introduce a deliberate bug into a linked list implementation. This project documents the process of finding the bug through systematic testing, fixing it, and understanding what it reveals about how AI generates pointer-based data structure code.

## Repository contents

| File | Description |
|---|---|
| `linked_list.py` | Clean reference implementation |
| `buggy_linked_list.py` | AI-generated version with deliberate bug, preserved as generated |
| `fixed_linked_list.py` | Corrected version after the bug was found |
| `test_buggy.py` | Test suite used to isolate the bug and verify the fix |
| `bug_hunt.md` | Hypotheses, findings, AI reveal comparison, lessons, and reflection |

## The bug

- **Location:** The `delete` method in `buggy_linked_list.py`.
- **What it does:** Deleting a non-head tail node leaves `self.tail` pointing to the detached node, so the next append is unreachable from `head`.
- **How I found it:** `test_delete_tail` deleted the tail and then appended another node, exposing the stale pointer.

## Run the investigation

Run the suite against the deliberately buggy implementation; exactly `test_delete_tail` should fail:

```bash
python3 test_buggy.py buggy_linked_list
```

Run it against the corrected implementation; every test should pass:

```bash
python3 test_buggy.py fixed_linked_list
```

## AI tool used

OpenAI Codex was used to generate the deliberate variation and as the AI participant whose reasoning was challenged and documented.
