# Graph Traversal Traces — AI Lab 11

Vertices are marked visited when first placed in the BFS queue or entered by
DFS. This prevents the shared vertex F from being scheduled twice.

## My Hand Traces — Before AI and Before Code

### BFS from A

- Initial: queue `[A]`, visited `{A}`, order `[]`.
- Process A: enqueue B, C; queue `[B, C]`, visited `{A, B, C}`, order `[A]`.
- Process B: enqueue D, E; queue `[C, D, E]`, visited `{A, B, C, D, E}`,
  order `[A, B]`.
- Process C: enqueue F; queue `[D, E, F]`, visited `{A, B, C, D, E, F}`,
  order `[A, B, C]`.
- Process D: queue `[E, F]`, visited unchanged, order `[A, B, C, D]`.
- Process E: F is already discovered; queue `[F]`, visited unchanged,
  order `[A, B, C, D, E]`.
- Process F: queue `[]`, visited unchanged, order `[A, B, C, D, E, F]`.
- Visiting order: **A → B → C → D → E → F**.

### DFS (recursive) from A

- Enter A: path `[A]`, visited `{A}`, order `[A]`.
- Enter B: path `[A, B]`, visited `{A, B}`, order `[A, B]`.
- Enter D: path `[A, B, D]`, visited `{A, B, D}`, order `[A, B, D]`;
  return to B.
- Enter E: path `[A, B, E]`, visited `{A, B, D, E}`, order `[A, B, D, E]`.
- Enter F from E: path `[A, B, E, F]`, visited `{A, B, D, E, F}`,
  order `[A, B, D, E, F]`; return through E and B to A.
- Enter C: path `[A, C]`, visited all vertices, order `[A, B, D, E, F, C]`.
- C sees F already visited and returns to A.
- Visiting order: **A → B → D → E → F → C**.

### My prediction

BFS uses FIFO queue order to finish the current distance level, while recursive
DFS uses the call stack to finish one neighbour path before trying its sibling.

## AI Traces

AI produced the same BFS and DFS orders and kept the queue, recursion path,
and visited set consistent at every step. It correctly said BFS discovers F
while processing C because C is dequeued before E. DFS reaches F from E while
still exploring B's subtree; when DFS later enters C, F is already visited.

## After AI and After Code

### Results

| Traversal | My order | AI's order | Actual order |
|---|---|---|---|
| BFS | A, B, C, D, E, F | A, B, C, D, E, F | A, B, C, D, E, F |
| DFS | A, B, D, E, F, C | A, B, D, E, F, C | A, B, D, E, F, C |

### Where my hand trace was right / wrong

The hand trace matched every queue and recursive-entry state in the program.
The point needing the most care was marking F visited when BFS enqueued it from
C; delaying that mark until removal could allow another parent to enqueue the
same vertex.

### Where the AI's trace was right / wrong

AI matched the program exactly and correctly timed F in both traversals. It
showed bookkeeping instead of skipping from the graph to a memorized final
order, which made the shared-vertex claim verifiable.

### The key insight

FIFO makes BFS process C before the deeper E path, so C discovers F. Recursive
DFS's LIFO call behavior remains inside B's subtree through D and E, letting E
reach F before DFS returns to explore C. The frontier discipline—not the graph
or total work—creates the different order.

## Reflection

The single design decision is how the frontier is removed: BFS takes the
oldest discovered vertex from a queue, while DFS continues with the newest
open call. That choice matters because level order supports shortest unweighted
paths and proximity questions, whereas depth order supports exhaustive path
exploration, backtracking, and structural tasks.

For a maze with unweighted edges, I would trust BFS and store parent links. It
first reaches F by the two-edge route A → C → F. DFS reaches F first through
A → B → E → F, so stopping at its first discovery would return a valid but
longer route.

AI's trace matched the program exactly, but that trust comes from comparing
its queue and path snapshots with the hand trace. A hand check is worth the
time when neighbour order, shared vertices, visited timing, or cycles can make
a plausible generic traversal order subtly wrong.
