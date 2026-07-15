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
