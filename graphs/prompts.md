# Prompt Log — AI Lab 11

## Prompt 1 — Trace BFS

**Prompt used:**

> Here is a directed graph as a Python adjacency list. Trace a breadth-first
> search starting from 'A', visiting neighbours in list order. Show the
> contents of the queue and the visited set after every single step, then give
> the final visiting order. Do not skip steps.
>
> graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [],
> 'E': ['F'], 'F': []}

**Why this prompt was structured this way:**

It demands queue and visited-set contents at every step so the simulation can
be checked rather than accepting only a final order.

## Prompt 2 — Trace DFS

**Prompt used:**

> Now trace a recursive depth-first search on the same graph from 'A', visiting
> neighbours in list order. Show the recursion path (which calls are open) and
> the visited set after every step, then give the final visiting order.

**Why this prompt was structured this way:**

Open-call paths expose exactly when recursion returns to a parent and moves to
the next sibling.

## Prompt 3 — Challenge the Shared Vertex

**Prompt used:**

> Vertex F is reachable from both C and E. In each of your two traces, which
> vertex causes F to be visited, and at what point? Explain why BFS and DFS
> reach F through different routes.

**Why this prompt was structured this way:**

F tests whether AI followed frontier and visited state or merely generated a
generic traversal order.

## Prompt 4 — Verification Script

**Prompt used:**

> Write a Python program that builds this graph, runs both BFS and DFS from
> 'A', and prints the visiting order of each. Implement BFS with a queue
> (collections.deque) and DFS recursively, both using a visited set. Print the
> two orders clearly labelled.

**Why this prompt was structured this way:**

It fixes the two implementation mechanisms and produces repeatable outputs for
comparison with both written traces.

## What I would change about these prompts next time

I would explicitly state whether "visited" means discovered or removed from
the frontier in Prompt 1, then request parent links so path claims can be
verified alongside visiting order.
