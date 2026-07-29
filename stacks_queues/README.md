# SE03 — AI Lab 04: Customer Support Ticket System

## What this repository is about

This directory is the deliverable for AI Lab 4 of the SE-03 Algorithmic
Thinking course. A customer support ticket system was designed using a
priority queue to satisfy two simultaneous ordering constraints: severity
level and arrival order within the same severity. AI was used as a design
partner to evaluate structure options, implement the system, and identify
likely failure modes, which were then verified through a structured test
suite.

## Repository contents

| File | Description |
|---|---|
| `ticket_system.py` | `TicketSystem` implementation using `heapq` |
| `test_ticket_system.py` | Tests for ordering, edge cases, and the spec |
| `design_notes.md` | Design, code review, results, and AI comparison |

## Design decision

- **Structure:** Priority Queue (`heapq`)
- **Why not FIFO queue:** Arrival order alone would let an older low-severity
  ticket block a newer critical ticket.
- **Why not stack:** LIFO order would process newer tickets first and provides
  no severity ordering.
- **Dual ordering solution:** Heap entries use `(severity, arrival_order)` so
  severity wins first and an incrementing counter breaks equal-severity ties.

## Test results

All seven required tests and two additional edge/extension tests pass.

## Running the project

```bash
python3 ticket_system.py
python3 test_ticket_system.py
```

## AI tool used

OpenAI Codex was used as the design and implementation partner.
