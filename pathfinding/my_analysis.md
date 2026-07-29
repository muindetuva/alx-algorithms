## My Predictions — Before AI and Before Code

### Naive greedy ("always take the cheapest next edge") from A to D

- Path it takes: A -> B -> D
- Total cost: 11

### The true shortest path from A to D

- Path: A -> C -> D
- Total cost: 8

### Why greedy fails here

- Greedy gets the first choice wrong by choosing A -> B only because it is the
  cheapest immediate edge. That local choice leads to a more expensive route
  overall, while A -> C costs slightly more at first but produces the lower
  total path to D.

## After AI and After Code

### Results table

| Strategy | Path A -> D | Total cost |
|---|---|---:|
| Naive greedy (my hand trace) | A -> B -> D | 11 |
| Naive greedy (AI) | A -> B -> D | 11 |
| Dijkstra's (Python output) | A -> C -> D | 8 |
| True shortest path | A -> C -> D | 8 |

### Where greedy went wrong

Greedy chose A -> B because its edge weight, 2, is lower than the weight 5
of A -> C. That choice is locally optimal, but it commits the route to the
expensive B -> D edge of weight 9. Taking A -> C initially costs more, yet its
following edge costs only 3, producing the lower total of 8.

### What the AI got right or wrong

The AI correctly traced both possible routes and identified A -> C -> D as the
minimum. More importantly, it identified the missing greedy-choice property:
a locally cheapest outgoing edge is not guaranteed to be part of a globally
shortest path. The explanation therefore went beyond merely comparing the two
totals.

### The principle

I should trust a greedy rule only after proving that every locally optimal
choice can be extended to a globally optimal solution. When that property is
absent, I should construct a counterexample and use an algorithm such as
Dijkstra's that compares the best complete cost discovered so far.

## Reflection

Naive greedy is greedy about the single cheapest edge leaving its current
vertex. Dijkstra's is greedy about the unvisited vertex with the smallest
total known distance from the start. That accumulated-distance choice matters
because it compares entire route prefixes rather than judging an edge in
isolation.

Dijkstra's requires non-negative weights. For example, adding A -> E with
weight 5, E -> B with weight -10, and B -> D with weight 2 can make a route
through a vertex that appeared expensive become cheaper after a negative
edge. A Dijkstra implementation that has already finalised B or D can then
miss the improvement. I would use Bellman-Ford for a graph with negative edge
weights, provided there is no reachable negative cycle when a finite shortest
path is required.

Before this lab, the cheapest visible next step could have seemed persuasive
for a routing problem. I will now test a greedy proposal with a small
counterexample and verify its greedy-choice property before relying on it.
