# BST Shape and Search Cost — AI Lab 10

Height in this analysis means the number of nodes on the longest root-to-leaf
path. With that convention, an empty tree has height 0 and a root-only tree
has height 1. The worst successful search performs one comparison per level.

## My Predictions — Before AI and Before Code

### Sequence A: 50, 25, 75, 10, 40, 60, 90

- Sketch:

  ```text
          50
         /  \
       25    75
      / \    / \
    10  40  60  90
  ```

- Height: 3 node levels.
- Worst-case search comparisons: 3.
- Classification: balanced.

### Sequence B: 10, 25, 40, 50, 60, 75, 90

- Sketch: `10 →right 25 →right 40 →right 50 →right 60 →right 75 →right 90`.
- Height: 7 node levels.
- Worst-case search comparisons: 7.
- Classification: degenerate; it is a right-only chain.

### Sequence C: 10, 90, 25, 75, 40, 60, 50

- Sketch:

  ```text
  10
    right → 90
             left → 25
                       right → 75
                                left → 40
                                          right → 60
                                                   left → 50
  ```

- Height: 7 node levels.
- Worst-case search comparisons: 7.
- Classification: degenerate despite alternating directions.

### My overall claim

Insertion order determines BST shape, so identical values can produce either
logarithmic-height search paths or a linear chain with O(n) worst-case search.

## AI Prediction and Reasoning

AI predicted heights 3, 7, and 7 for A, B, and C. For Sequence B it correctly
explained that every new maximum follows only right links, making the tree
equivalent to a singly linked list with O(n) search rather than balanced-tree
O(log n) search.

For Sequence C, AI traced the final value 50 through comparisons with 10, 90,
25, 75, 40, and 60 before attaching it as the left child of 60. That trace
confirmed the mixed-looking order still creates a seven-node zig-zag chain.

## After AI and After Code

### Results table

| Sequence | Predicted height | AI's height | Actual height | Worst-case search |
|---|---:|---:|---:|---:|
| A | 3 | 3 | 3 | 3 comparisons |
| B | 7 | 7 | 7 | 7 comparisons |
| C | 7 | 7 | 7 | 7 comparisons |

### Where I was right

All three height, shape, and worst-case cost predictions matched the program.
I correctly treated Sequence C as a chain rather than assuming that a mixed
insertion order automatically creates balance.

### Where I was wrong

None of the final predictions was wrong. The main ambiguity was terminology:
some sources count height in edges and would report 2, 6, and 6. Defining
height as node levels before predicting avoided mistaking a convention
difference for a structural disagreement.

### Where the AI was right or wrong

AI was correct on every shape and clearly traced each comparison for the late
insertion of 50. It did not merely label C "unbalanced"; it placed 50 beneath
60 and identified the full root-to-leaf path. Its only required clarification
was which height convention to use.

### The key insight

A plain BST enforces value ordering but does not enforce balance. Insertion
order controls height, and search cost follows height: Sequence A uses three
comparisons at worst, while B and C can require all seven despite holding the
same sorted set of values.

All three in-order traversals are identical:
`[10, 25, 40, 50, 60, 75, 90]`.

## Reflection

The data values determine the BST's in-order result, but the links created by
insertion determine how many nodes a search must traverse. Two structures can
represent the same set while offering very different performance because
layout, balance, indexing, and access paths are separate from content.

Sorted timestamps, auto-incrementing IDs, sequential event numbers, and
alphabetically imported records can arrive in monotonic order and turn a plain
BST into a chain. A production system should use a self-balancing tree such as
AVL or red-black, randomise insertion order when appropriate, bulk-build a
balanced tree, or choose a hash table when ordering is unnecessary.

AI traced the insertions correctly, including Sequence C's alternating chain
and the final placement of 50. That result increases confidence only because
the trace exposed each comparison for manual checking; a generic "mixed means
partly balanced" answer would have been easy to accept and wrong. Hand checks
are worthwhile whenever one missed branch changes a structural conclusion.
