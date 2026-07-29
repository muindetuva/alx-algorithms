# LIS Analysis — AI Lab 8

## Step 1: DP Recognition Checklist

### Does the problem ask for an optimum or count?

Yes. It asks for the maximum length among all strictly increasing
subsequences whose elements retain their original order.

### Can it be expressed as a recurrence?

Yes. Define `LIS(i)` as the longest increasing subsequence ending exactly at
index `i`. Any earlier index `j` whose value is smaller can precede `i`, so a
candidate length is `LIS(j) + 1`. The best eligible predecessor determines
`LIS(i)`.

### Do subproblems overlap?

Yes. Computing both `LIS(5)` and `LIS(6)` can request results such as `LIS(0)`,
`LIS(2)`, and `LIS(3)`. Without a cache, those same ending-index states would
be recomputed along multiple recursive paths.

### Does greedy fail?

Yes. On `[3, 1, 2]`, a rule that starts with 3 and only accepts the next larger
value returns length 1 because neither 1 nor 2 can extend 3. The optimal choice
skips 3 and takes `[1, 2]`, giving length 2. A locally valid starting choice can
block the global optimum.

### My verdict

DP applies. LIS asks for an optimum, has optimal substructure through eligible
predecessors, and repeats the same ending-index subproblems.

### My recurrence (before asking AI)

`LIS(i) = 1 + max(LIS(j))` for every `j < i` where
`nums[j] < nums[i]`. If there is no eligible `j`, `LIS(i) = 1` because the
element at `i` forms a one-element subsequence. The full answer is
`max(LIS(i))` over every index, or 0 for an empty input.

## Recurrence Verification

### Was my recurrence correct?

Yes. The state, strict comparison, default value, and final maximum were all
necessary and correctly included.

### If not — what was wrong and what is the correct recurrence?

No correction was required. AI emphasized that taking only `LIS(n - 1)` would
be incorrect because the longest subsequence need not end at the final index.

### The correct recurrence

`LIS(i) = max(LIS(j) + 1)` for all `j < i` where
`nums[j] < nums[i]`.

Base case: `LIS(i) = 1` for every index when no eligible predecessor exists.

## Memoised Solution Review

### Cache key used

The key is index `i`. Each value stores the LIS length ending at that exact
index. The wrapper creates a fresh dictionary for each input so indices from
different lists cannot be mixed.

### Base case — correct?

Yes. `best` starts at 1, so index 0 and any later value with no smaller
predecessor return 1. The wrapper separately returns 0 for an empty list.

### Recursive case — correct?

Yes. It visits only `previous < i`, recurses only when
`nums[previous] < nums[i]`, adds the current element, and caches the maximum.

### Any issues I spotted before running

The recursive call counter includes cache hits, which is appropriate for
measuring invocations but is larger than the number of unique computations.
Recursion depth can also reach O(n) on an increasing input.

### Cache trace for `[10, 9, 2, 5, 3, 7, 101, 18]`

The shared cache after each newly computed ending index is:

```text
i=0: {0: 1}
i=1: {0: 1, 1: 1}
i=2: {0: 1, 1: 1, 2: 1}
i=3: {0: 1, 1: 1, 2: 1, 3: 2}
i=4: {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
i=5: {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3}
i=6: {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 4}
i=7: {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 4, 7: 4}
```

### Memoised test results

| Input | Expected | Result | Recursive calls |
|---|---:|---:|---:|
| `[10, 9, 2, 5, 3, 7, 101, 18]` | 4 | 4 | 25 |
| `[0, 1, 0, 3, 2, 3]` | 4 | 4 | 17 |
| `[7, 7, 7, 7]` | 1 | 1 | 4 |

## Tabulated Solution Review

The DP array initializes every entry to 1. The outer loop moves left to right,
the inner loop checks all earlier indices, and only a strict `<` comparison can
extend a subsequence. The function returns `max(dp)`, not `dp[-1]`, and handles
an empty list separately.

For the first example, the table states are:

```text
initial: [1, 1, 1, 1, 1, 1, 1, 1]
i=0:     [1, 1, 1, 1, 1, 1, 1, 1]
i=1:     [1, 1, 1, 1, 1, 1, 1, 1]
i=2:     [1, 1, 1, 1, 1, 1, 1, 1]
i=3:     [1, 1, 1, 2, 1, 1, 1, 1]
i=4:     [1, 1, 1, 2, 2, 1, 1, 1]
i=5:     [1, 1, 1, 2, 2, 3, 1, 1]
i=6:     [1, 1, 1, 2, 2, 3, 4, 1]
i=7:     [1, 1, 1, 2, 2, 3, 4, 4]
```

Both approaches use O(n²) time because each index considers every earlier
index. Tabulation uses O(n) space for `dp`; memoisation uses O(n) cache space
plus an O(n) worst-case recursion stack.

## Memoised vs Tabulated — Comparison

### Time complexity

- Memoised: O(n²), because all n ending states scan up to n predecessors.
- Tabulated: O(n²), for the same nested predecessor checks.
- Same / different: asymptotically the same, although tabulation avoids
  function-call and dictionary-lookup overhead.

### Space complexity

- Memoised: O(n) cache plus an O(n) worst-case recursion stack.
- Tabulated: O(n) DP array and O(1) additional loop state.
- Same / different: both are O(n) asymptotically, but memoisation has a larger
  constant and stack-depth risk.

### AI's recommendation

AI recommended tabulation for production LIS because it avoids recursion
limits, has smaller constant factors, and expresses the left-to-right
dependency directly.

### My recommendation

I agree. Tabulation is clearer for this recurrence, computes exactly the states
needed for the final maximum, and does not risk `RecursionError` on long input.

### A case where I would choose the other approach

I would choose memoisation for a variant that asks about only a small subset of
ending indices or has sparse, irregular transitions, because top-down
evaluation can skip unreachable states. For the standard full LIS length, the
wrapper needs every ending index, so that advantage does not apply.

## Edge Case: All Equal Elements

### Expected answer

The answer for `[5, 5, 5, 5, 5]` is 1. Strictly increasing requires `<`, so an
equal value cannot extend a subsequence.

### Trace of dp array

```text
initial: [1, 1, 1, 1, 1]
i=0:     [1, 1, 1, 1, 1]
i=1:     [1, 1, 1, 1, 1]
i=2:     [1, 1, 1, 1, 1]
i=3:     [1, 1, 1, 1, 1]
i=4:     [1, 1, 1, 1, 1]
```

### Both implementations correct? Y/N

Yes. Both return 1, and both also pass the empty and single-element cases.

### If not — what was wrong?

No correction was needed. Both implementations use strict `<`; changing that
condition to `<=` would incorrectly treat equal values as increasing.

## Reflection

The O(n log n) patience-sorting approach works differently from the O(n²) DP
recurrence. It greedily maintains the smallest possible tail for each length
and uses binary search to replace a tail; it does not repeatedly solve
overlapping `LIS(i)` states. Its correctness still relies on a global optimal
invariant, but the DP overlap diagnostic does not describe its mechanism.

AI did acknowledge one situation for choosing memoisation—an on-demand or
sparse-state variant—but correctly explained why it offers little benefit for
standard LIS. This balanced recommendation came only after the prompt required
a concrete opposite case, showing that design questions need explicit
trade-off criteria more than factual recurrence questions do.

Splitting the DP story across Labs 7 and 8 was useful. Measuring the waste of
naive recursion first created a concrete reason to care about caching, while
this lab could focus on recognizing and implementing both fixes. I learn best
when a performance problem is observed and explained before the optimized
pattern is introduced.
