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
