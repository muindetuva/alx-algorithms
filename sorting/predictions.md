# Sorting Benchmark Predictions — AI Lab 6

## My Predictions — Before AI

For each dataset, rank the five algorithms from fastest (1) to slowest (5).
Use: Bubble, Insertion, Merge, Quicksort (random pivot), Timsort

### Dataset A — 10,000 random integers

Predicted ranking: 1. Timsort 2. Quicksort (random pivot) 3. Merge 4. Insertion 5. Bubble

Reasoning:

For random integers, the O(n log n) algorithms should be much faster than the O(n²) algorithms. Timsort is highly optimized in Python, so I expect it to be fastest. Quicksort with a random pivot should also perform well on random data. Merge sort should be reliable but may have extra memory overhead. Insertion sort and bubble sort should be much slower because random data gives them many comparisons and swaps.

### Dataset B — Already sorted ascending

Predicted ranking: 1. Timsort 2. Insertion 3. Merge 4. Quicksort (random pivot) 5. Bubble

Reasoning:

Timsort should be fastest because it is designed to detect and exploit already sorted runs. Insertion sort also has its best case here because each item is already in the correct place, so it should run close to O(n). Merge sort and random-pivot quicksort still do more general divide-and-conquer work. Bubble sort can be fast only if it has an early-exit optimization; without that, it remains very slow.

### Dataset C — Sorted descending

Predicted ranking: 1. Timsort 2. Merge 3. Quicksort (random pivot) 4. Insertion 5. Bubble

Reasoning:

Timsort should still do well because descending runs can be detected and reversed. Merge sort should be stable and predictable at O(n log n). Random-pivot quicksort should avoid the worst case that a fixed-pivot quicksort might hit. Insertion sort should be very slow because every item has to move across many earlier items. Bubble sort should also be very slow because descending order creates many swaps.

### Dataset D — Nearly sorted (100 random swaps)

Predicted ranking: 1. Timsort 2. Insertion 3. Merge 4. Quicksort (random pivot) 5. Bubble

Reasoning:

Timsort should exploit existing order most aggressively, so I expect it to win. Insertion sort should also perform well because most elements are close to where they belong. Merge sort and quicksort do not benefit as much from near-sorted input in a simple implementation. Bubble sort may improve slightly if optimized with early exit, but random swaps can still force repeated passes.

### Dataset E — High duplicates (90% same value)

Predicted ranking: 1. Timsort 2. Merge 3. Quicksort (random pivot) 4. Insertion 5. Bubble

Reasoning:

This is tricky because equal elements can affect partitioning. Timsort should still perform well because repeated values may form easy runs. Merge sort should handle duplicates consistently. Random-pivot quicksort may be slower if the partitioning does not handle many equal values efficiently, because equal elements can create unbalanced partitions depending on the implementation. Insertion sort may benefit from fewer movements when many values are equal, but it is still generally O(n²). Bubble sort is likely slowest.

## My Overall Prediction

I think Dataset C, sorted descending, will show the largest performance gap between the fastest and slowest algorithm.

My reason is that Timsort can detect ordered runs and may handle descending data efficiently, while bubble sort and insertion sort face close to their worst-case behavior because many elements need to move a long distance. That should create a very large gap between the best adaptive algorithm and the slowest quadratic algorithm.

## AI Predictions vs Mine — Before Benchmarking

### Where we agreed

We both expected Timsort to win every dataset because it is implemented in
optimized C and adapts to existing runs. We also placed Bubble and Insertion
near the bottom for random and reverse-sorted data, and expected Merge to be
predictably competitive without adapting much to input order.

### Where we disagreed

The AI placed early-exit Bubble ahead of Merge and Quicksort on the already
sorted dataset because Bubble needs only one linear pass. My ranking left
Bubble last despite explicitly noting the optimization. The AI also expected
a three-way Quicksort to handle high duplicates better than Merge, while my
initial ranking put Merge ahead without conditioning the prediction on the
partition strategy.

### AI reasoning that was better than mine

It separated algorithmic complexity from implementation details. In
particular, it noted that Python's built-in sort runs in C while all custom
implementations run in Python, and that Quicksort's duplicate performance
depends on whether equal values form their own partition.

### My reasoning that the AI missed or glossed over

The AI treated random-pivot Quicksort as if random pivot selection guaranteed
consistent timings. Pivot choice still introduces run-to-run variance, and
recursive list construction adds allocation costs that Big O notation does
not show.

## Actual Benchmark Results

All datasets contained 10,000 values. Bubble and Insertion were measured once
per dataset because of their quadratic cost; Merge, Quicksort, and Timsort use
the median of three `timeit` runs.

### Dataset A — Random

| Algorithm | Time (s) | Rank |
|---|---:|---:|
| Bubble | 3.187942 | 5 |
| Insertion | 1.389208 | 4 |
| Merge | 0.015890 | 3 |
| Quicksort | 0.008768 | 2 |
| Timsort | 0.000598 | 1 |

### Dataset B — Already Sorted Ascending

| Algorithm | Time (s) | Rank |
|---|---:|---:|
| Bubble | 0.000357 | 2 |
| Insertion | 0.000668 | 3 |
| Merge | 0.010033 | 5 |
| Quicksort | 0.008171 | 4 |
| Timsort | 0.000025 | 1 |

### Dataset C — Sorted Descending

| Algorithm | Time (s) | Rank |
|---|---:|---:|
| Bubble | 4.278350 | 5 |
| Insertion | 2.833887 | 4 |
| Merge | 0.010622 | 3 |
| Quicksort | 0.008967 | 2 |
| Timsort | 0.000029 | 1 |

### Dataset D — Nearly Sorted

| Algorithm | Time (s) | Rank |
|---|---:|---:|
| Bubble | 1.834949 | 5 |
| Insertion | 0.037608 | 4 |
| Merge | 0.012853 | 3 |
| Quicksort | 0.008166 | 2 |
| Timsort | 0.000074 | 1 |

### Dataset E — High Duplicates

| Algorithm | Time (s) | Rank |
|---|---:|---:|
| Bubble | 2.100595 | 5 |
| Insertion | 0.252483 | 4 |
| Merge | 0.015096 | 3 |
| Quicksort | 0.000727 | 2 |
| Timsort | 0.000188 | 1 |

### Largest performance gap observed

Dataset C had the largest gap. Bubble took 4.278350 seconds while Timsort took
0.000029 seconds, an approximate 147,529× difference based on the displayed
timings.

## Interrogating the Surprise

### What surprised me most

Bubble was second-fastest on Dataset B despite ranking last on every other
dataset. It even beat Insertion, Merge, and randomized Quicksort on that one
input shape.

### The AI's explanation of why

Early-exit Bubble performs one pass over a sorted list, observes no swaps, and
stops. That changes its sorted-input behavior from quadratic to O(n). Merge
and Quicksort still recursively partition and combine the entire list, while
Insertion also has an O(n) best case but performs more Python-level loop work
per item in this implementation.

### My assessment: was the explanation correct, complete, or missing something?

The explanation was correct and mostly complete. It identified Bubble's best
case and the non-adaptive work of the divide-and-conquer implementations. The
important additional detail is that Timsort runs in optimized C, so equal Big
O best cases do not imply equal elapsed time for these Python functions.

### What this reveals about that algorithm's behaviour

Bubble's poor general reputation does not erase its linear best case when an
early-exit flag is present. That narrow advantage disappears as soon as a few
far-apart elements force repeated passes, as Dataset D demonstrates.

## Reflection

My Dataset A ranking matched the actual order exactly. Dataset B was my worst
prediction because I placed Bubble last even after noting its early-exit
optimization; it actually ranked second. My mental model of asymptotic cases
was sound, but I did not consistently translate implementation details into a
complete ranking.

On Dataset E, three-way Quicksort was far faster than I predicted and beat
Merge by more than 20×. Its equal partition collects the 9,000 repeated values
without recursively sorting them, while Merge still performs its full merge
structure. Insertion and Bubble make fewer movements when values compare
equal, but shuffled outliers still cause substantial quadratic-style work.

Forming a hypothesis produced the most value in this sorting lab because the
rankings were precise and directly falsifiable across five controlled input
shapes. The measurements exposed exactly where I understood an algorithm's
case analysis but failed to account for early exit, three-way partitioning,
language overhead, or adaptive behavior.
