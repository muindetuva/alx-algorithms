# Prompt Log — AI Lab 12

## Prompt 1 — Greedy Result

**Prompt used:**

> Here is a weighted directed graph as a Python adjacency list, where each
> pair is (neighbour, weight). Using a naive greedy strategy — from the
> current vertex, always take the cheapest outgoing edge — trace the path
> from A to D step by step and give its total cost. Do not use Dijkstra's
> algorithm yet; just follow the naive greedy rule.
>
> graph = {'A': [('B', 2), ('C', 5)], 'B': [('D', 9)],
> 'C': [('D', 3)], 'D': []}

**Why this prompt was structured this way:**

I explicitly forbade Dijkstra's so the naive rule would be followed and the
greedy trap would remain visible instead of being replaced by the correct
shortest-path algorithm.

## Prompt 2 — True Shortest Path

**Prompt used:**

> Now find the actual shortest path from A to D by total weight, considering
> all routes. Show the total cost of each possible path and identify the
> minimum.

**Why this prompt was structured this way:**

Requiring every possible route and its total makes the comparison auditable
and prevents a correct answer with unsupported reasoning.

## Prompt 3 — Challenge the Reasoning

**Prompt used:**

> Naive greedy chose the edge A→B because it was cheaper than A→C. Explain
> precisely why that locally optimal choice led to a globally worse result,
> and state the general property a problem must have for greedy to be safe —
> which this graph lacks.

**Why this prompt was structured this way:**

The question asks for the greedy-choice property so the response must explain
the general failure rather than only repeat the route costs.

## Prompt 4 — Dijkstra's Implementation

**Prompt used:**

> Write a Python implementation of Dijkstra's algorithm using heapq that
> takes this adjacency list and a start vertex, and returns the shortest
> distance from the start to every vertex. Then call it on this graph from
> 'A' and print the result.

**Why this prompt was structured this way:**

It fixes the required priority-queue implementation and requests all shortest
distances, providing concrete output against which the hand prediction can be
checked.

## What I would change about these prompts next time

I would ask the implementation prompt to return predecessors from the start,
not only distances, so both the route and cost could be verified immediately.
I would also request explicit rejection of negative weights.
