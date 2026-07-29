# Search Strategy Analysis — AI Lab 9

## My Assessment — Before AI

### The problem characteristics

- Dataset size: 50,000 elements
- Is the data sorted? No
- How many searches will be performed? Four targets will each be searched
  repeatedly during the benchmark, so setup can be amortised over many calls.
- Will the dataset change between searches? The supplied catalogue is static.

### Applying the decision framework

#### How many times will I search this collection?

The lab performs 4,000 measured lookups, so this is repeated search rather
than one isolated query.

#### Does the data need ordered access?

No. The requirement is membership only; it does not ask for ranges, nearest
values, or ordered traversal.

#### Are the keys hashable?

Yes. Python integers are hashable and work directly as set entries.

#### Is memory constrained?

No memory constraint is stated. A set uses more memory than the original list,
but 50,000 integers are reasonable for this scenario.

### My recommended strategy

Build a hash set once, then use membership tests. Its O(n) setup is amortised
over thousands of lookups, each expected O(1), and the task does not need the
ordering that would justify sorting.

### My predicted complexity for each approach

| Approach | Setup cost | Per-search cost | Total for 4 searches |
|---|---|---|---|
| Linear search | O(1) | O(n) | O(4n) = O(n) |
| Sort + binary search | O(n log n) | O(log n) | O(n log n + 4 log n) |
| Hash set | O(n) | O(1) average | O(n + 4) = O(n) |

### Which approach would I NOT use and why

I would not sort solely for four membership queries. It pays O(n log n) setup
on unsorted data and provides ordering that the feature does not require. It
becomes attractive only if ordered operations or many searches justify that
setup and a set's extra memory is undesirable.

## AI's Initial Recommendation

### Strategy AI recommended

AI recommended building a hash set once and using membership lookup.

### Assumptions AI stated explicitly

It stated that the catalogue would receive repeated searches, product IDs are
hashable, and O(n) construction could be amortised over those queries.

### Assumptions AI made WITHOUT stating them

It initially left three assumptions implicit: enough memory exists for another
50,000-entry structure, the catalogue stays unchanged after the set is built,
and only exact membership—not ordered or range access—is required.

### Did AI consider all three strategies (linear, binary, hash)?

Yes. It compared no-setup linear search, sort-once binary search, and a
build-once hash set before selecting the set for repeated membership queries.

### Do I agree with AI's recommendation? Why or why not?

Yes, for the benchmark's static catalogue and thousands of searches. The
recommendation would need revisiting if searches were rare, memory were tight,
or the catalogue changed without synchronising the cache.

## Assumption Challenge Results

### Scenario 1: 4 searches, never again

- Did AI change its recommendation? Yes. It revised the default to a linear
  scan because four queries may not justify another data structure.
- Was the revised recommendation correct? Yes. Hash and linear are both O(n)
  overall, but linear avoids allocation and may stop early for present values.
- Total cost analysis (my calculation):
  - Linear: O(n) × 4 = O(4n) = O(n), with no setup.
  - Sort + binary: O(n log n) + O(4 log n) = O(n log n).
  - Hash set: O(n) + O(4) = O(n).
  - Winner for four searches: linear or hash are roughly comparable; sorting
    is worst when ordered access has no other value.

### Scenario 2: frequent updates

- Did AI change its recommendation? It retained a hash-based strategy but
  changed from rebuilding a cached set to maintaining the set alongside the
  source catalogue.
- Was the revised recommendation correct? Yes, assuming updates can modify the
  set transactionally so the two structures remain consistent.
- Why frequent updates favour hash set over sorted list: set insertion and
  deletion are expected O(1), while inserting into or removing from a sorted
  Python list is O(n) because elements shift. Re-sorting snapshots would cost
  O(n log n) repeatedly.

## Benchmark Results

### Setup times (one-time cost)

| Approach | Setup time (s) |
|---|---:|
| Linear | 0.00000000 |
| Sort + binary | 0.00397155 |
| Hash set | 0.00074380 |

Setup was measured from each prepared strategy's first call, less one warmed
lookup estimate so the displayed value isolates construction work.

### Search times (per search, averaged over 1,000 runs)

| Target | Linear (s) | Binary (s) | Hash (s) |
|---|---:|---:|---:|
| present_early | 0.00000084 | 0.00000024 | 0.00000006 |
| present_middle | 0.00021905 | 0.00000022 | 0.00000007 |
| present_late | 0.00044556 | 0.00000023 | 0.00000007 |
| absent | 0.00042329 | 0.00000022 | 0.00000007 |

### Total time (setup + 4 searches × 1,000 runs)

| Approach | Total time (s) | Relative to hash |
|---|---:|---:|
| Linear | 1.08874167 | 1,076.08× |
| Sort + binary | 0.00487822 | 4.82× |
| Hash set | 0.00101176 | 1.00× |

### Most interesting observation

Even the early linear target at index 100 was slower than binary search. The
target was early relative to 50,000 entries, but not early enough to overcome
101 Python-level comparisons versus roughly 16 comparisons in C-backed bisect.

## Interrogating the Surprising Result

### What surprised me

I expected linear search to beat binary search for `present_early` because it
terminates at index 100, but linear averaged 0.84 µs and binary averaged only
0.24 µs after setup.

### AI's explanation

Linear search does benefit from early termination, but "early" here still
means checking about 101 IDs in a Python loop. Binary search examines about
`log2(50,000)`, or 16, positions regardless of where the target appeared in
the original unsorted list. Python's `bisect_left` also uses a C implementation,
so its loop and index arithmetic avoid most Python-level per-iteration cost.

### Was the explanation correct and complete?

Yes. It addressed early termination, binary's position-independent logarithmic
comparison count, and the implementation constant. It also correctly noted
that binary's result excludes its one-time sort; including setup reverses the
decision for a single early query.

### What this reveals about when theoretical complexity differs from practical performance

Asymptotic bounds describe growth, not an exact stopwatch result. Input
position, number of queries, preprocessing, language implementation, and
constant factors determine where one strategy overtakes another. Linear could
still win for an item in the first few positions, but index 100 was beyond that
machine- and implementation-specific crossover here.

## Reflection

The initial AI response stated repeated-search and hashability assumptions but
silently assumed available memory, a stable catalogue, and membership-only
queries. Unstated assumptions matter because a recommendation can be
technically sound under one workload yet fail when updates, ordering, memory,
or consistency requirements are revealed later.

Hash lookup was fastest for every warmed target, but binary beating the early
linear scan does not make linear or binary inherently bad. Binary guarantees
logarithmic comparisons after sorted setup; linear has no setup and can win on
very early matches. The result shows that Big O must be combined with workload
shape, preprocessing cost, and implementation constants.

The measurements confirm the theoretical decision framework: repeated exact
membership favored hashing, sorted lookup provided predictable O(log n)
searches after a larger setup, and linear time grew with target position. The
theory did not incorrectly predict the early-target stopwatch result—it never
promised that all O(n) calls are slower than all O(log n) calls. That difference
came from early termination and CPython's C-backed bisect constant factors.
