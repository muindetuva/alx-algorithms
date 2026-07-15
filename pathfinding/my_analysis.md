## My Predictions — Before AI and Before Code

### Naive greedy ("always take the cheapest next edge") from A to D

- Path it takes: A -> B -> D
- Total cost: 11

### The true shortest path from A to D

- Path: A -> C -> D
- Total cost: 4

### Why greedy fails here

- Greedy gets the first choice wrong by choosing A -> B only because it is the cheapest immediate edge. That local choice leads to a more expensive route overall, while A -> C costs slightly more at first but produces the lower total path to D.
