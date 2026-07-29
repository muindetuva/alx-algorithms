# Design Notes — AI Lab 4

## My Recommendation — Before AI

### Which structure would I use and why?

I would use a priority queue, with a queue-like ordering inside each priority level.

This matches the requirements because tickets do not only need to be handled in arrival order. They also need to be handled by severity. A priority queue lets the system choose Critical tickets before High, Medium, and Low tickets. To preserve arrival order within the same severity, each ticket should also store an arrival number or timestamp.

Against the five requirements:

- Tickets arrive continuously: new tickets can be inserted into the priority queue as they arrive.
- Each ticket has a severity level: the severity becomes the main priority value.
- Critical and High must be handled before Medium and Low: lower severity numbers should be processed first.
- Same severity uses arrival order: arrival order becomes the tie-breaker.
- Agents process one ticket at a time: when an agent is free, the system removes the next highest-priority ticket.
- The system reports waiting tickets: keep a count of queued tickets or use the size of the queue.
- Tickets should never be lost: tickets stay in the priority queue until an agent removes them for processing.

### How does my structure handle the two ordering constraints?

- Constraint 1: Higher severity tickets processed before lower severity

The priority queue compares tickets by severity first. Since Critical is `1`, High is `2`, Medium is `3`, and Low is `4`, smaller severity numbers should come out first.

- Constraint 2: Within the same severity, earlier tickets processed first

Each ticket should include an arrival order value, such as an incrementing counter. If two tickets have the same severity, the priority queue compares their arrival order. The lower arrival number came first, so it should be processed first.

### How would I represent a ticket?

I would represent each ticket as a dictionary or small object with these fields:

```python
{
    "id": "A",
    "customer": "customer@example.com",
    "message": "Cannot log in",
    "severity": 1,
    "arrival_order": 0
}
```

The `severity` field controls priority. The `arrival_order` field preserves first-in, first-out behavior among tickets with the same severity. The `id`, `customer`, and `message` fields carry the support information agents need.

### Edge cases I need to handle

- An agent asks for the next ticket when no tickets are waiting.
- Many Critical tickets arrive and lower-priority tickets wait for a long time.
- Two tickets have the same severity and arrive very close together.
- A ticket has an invalid severity, such as `0`, `5`, or a string.
- Tickets arrive faster than agents can process them, so the queue grows large.
- The system must report the waiting count correctly after tickets are added and removed.

### Why a plain FIFO queue would not work here

A plain FIFO queue only processes tickets in arrival order. That would break the severity requirement. For example, if a Medium ticket arrives at 09:00 and a Critical ticket arrives at 09:05, FIFO would process the Medium ticket first. The system requires the Critical ticket to be handled first, so plain FIFO is not enough.

### Why a stack would not work here

A stack processes the most recently added item first. That would break arrival order within the same severity because newer tickets would be handled before older tickets. It would also not automatically handle severity priority. A stack is useful for last-in, first-out behavior, but support tickets need priority ordering plus first-in, first-out ordering within each priority.

## AI Design Conversation

The AI compared a FIFO queue, a stack, and a priority queue. It reached the
same recommendation: use a min-heap whose first comparison value is severity
and whose second value is an incrementing arrival counter. A FIFO queue cannot
promote a newer critical ticket, while a stack reverses arrival order and also
lacks severity handling.

For two Critical tickets, the heap entries begin with severity `1`. Because
that value ties, the heap compares the arrival counters. The first Critical
ticket has the smaller counter and therefore leaves the heap first.

### Likely failure modes identified by AI

1. Omitting the arrival counter could order equal-severity tickets by an
   unrelated field or attempt to compare non-orderable ticket objects.
2. Accepting severity values outside 1–4 could silently produce invalid
   priorities and unexpected processing order.
3. Popping or peeking an empty heap without an explicit check could expose a
   low-level error instead of a clear ticket-system error.

## Code Review — Before Running

### Tiebreaker present?

Yes. Every heap entry contains severity first and a unique incrementing
arrival number second. The `Ticket` object is third and never needs to be
compared.

### Empty queue handling?

Yes. Both `process_next` and `peek_next` check `is_empty` and raise an
`IndexError` with a clear message when no tickets are waiting.

### Demonstration output matches expected?

The demonstration submits A, B, C, and D in the specified order. Reading the
heap rules predicts the required output: B → D → C → A.

### Anything suspicious?

The main risks worth testing are stability for equal severities, whether
`peek_next` changes the queue, invalid severity input, and whether the optional
`get_all_waiting` method accidentally removes entries.

## Test Results

| Test | Pass / Fail |
|---|---|
| severity_ordering | Pass |
| arrival_order_within_same_severity | Pass |
| scenario_from_spec | Pass |
| process_next_on_empty | Pass |
| peek_next_does_not_remove | Pass |
| tickets_waiting_count | Pass |
| single_ticket | Pass |
| get_all_waiting | Pass |
| invalid_severity | Pass |

### Root cause of any failures

No test failed. The implementation included the stable arrival-order
tiebreaker before the first run, so the most likely ordering defect was not
present.

### Fix applied

No post-test fix was needed. The key preventive design choice was storing each
heap entry as `(severity, arrival_order, ticket)`, which makes the heap compare
the two required ordering keys before it reaches the ticket object.

### Did the AI's predicted failure modes from Prompt 4 match what I found?

The predicted risks matched the cases that needed the most scrutiny, even
though none became an observed failure. The tests confirmed stable tie
breaking, intentional empty-queue errors, rejected invalid severities, and a
non-destructive queue inspection method.

## Reflection

A priority queue ordered only by severity cannot promise FIFO behavior when
two priorities tie; it needs another comparable value and might otherwise
compare unrelated ticket data. An incrementing index is unique, increases in
the exact submission order, and therefore makes the earlier equal-severity
ticket sort first.

Across the four labs, AI has been most reliable when comparing named design
alternatives against explicit requirements because each claim can be checked
one requirement at a time. Implementation and debugging require the most
critical oversight: code that looks plausible can still mishandle an edge
case, mutate data unexpectedly, or hide an incorrect assumption that only a
targeted test reveals.

A hospital emergency department likely uses priority-queue behavior when
triaging patients. Medical urgency is its equivalent of ticket severity,
while arrival or triage time can break ties between patients at the same
urgency level.
