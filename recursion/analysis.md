# Coin Change Analysis — AI Lab 7

## My Implementation — Before AI

The implementation follows the problem definition directly. An amount of zero
needs no more coins, a negative amount is impossible, and every positive
amount branches once for each denomination before choosing the best result.

### My call counts

| amount | result | calls made |
|---:|---:|---:|
| 6 | 2 | 29 |
| 11 | 2 | 137 |
| 36 | 3 | 296,969 |
| 41 | 4 | 1,372,261 |
| 20 | 2 | 2,221 |
| 30 | 2 | 47,325 |
| 40 | 3 | 1,010,369 |
| 50 | 2 | 21,575,601 |

### My observations

Before measuring, I expect the call count to grow exponentially rather than
linearly because each positive amount launches up to four recursive calls.
The recursion tree can contain the same remaining amount along many paths. A
loose upper bound is O(4^amount) for four denominations and minimum coin 1,
although negative base cases prune many branches earlier.

### My hypothesis about where the overlap is

I expect `coin_change(1)` and `coin_change(0)` to be recomputed most often.
Many different sequences of chosen coins eventually reach these small amounts,
and the naive function has no stored result that lets one branch reuse work
already completed by another branch.

After measuring, the call counts confirm the expected exponential pattern.
Increasing the amount from 40 to 50 multiplies the calls by more than 21,
despite adding only ten to the input. Amount 50 took 3.7420 seconds for one
call and was the first tested value that felt noticeably slow; I stopped there
rather than testing larger values.

## AI Explanation of the Repeated Work

The AI identified remaining amount as the complete recursive state because the
coin list never changes. Different sequences can reach the same state: when
solving amount 11, the branch through amount 10 can later request amount 5,
while the branch through amount 6 requests amount 5 immediately. Neither
branch remembers that the other has already solved it.

The first two levels it described for amount 11 were:

```text
coin_change(11)
├── use 1: coin_change(10)
│   ├── coin_change(9)
│   ├── coin_change(5) ⭐
│   ├── coin_change(0) ⭐
│   └── coin_change(-15)
├── use 5: coin_change(6)
│   ├── coin_change(5) ⭐
│   ├── coin_change(1) ⭐
│   ├── coin_change(-4)
│   └── coin_change(-19)
├── use 10: coin_change(1) ⭐
│   ├── coin_change(0) ⭐
│   ├── coin_change(-4)
│   ├── coin_change(-9)
│   └── coin_change(-24)
└── use 25: coin_change(-14)
```

It classified the time complexity as exponential. A loose upper bound is
O(c^(A/s)), where c is the number of coin types, A is the amount, and s is the
smallest denomination. With four coins including 1, that can be written as
O(4^A), although negative branches make the measured growth smaller than this
upper bound. It predicted that amounts around 45–50 would become noticeable on
a typical machine, which matched the 3.742-second result at 50.

## My Call Tree Trace — coin_change([1, 5], 6)

The full trace below includes the first three levels and continues to the base
cases so repeated states can be counted exactly:

```text
coin_change(6)
├── try 1: coin_change(5)
│   ├── try 1: coin_change(4)
│   │   ├── try 1: coin_change(3)
│   │   │   ├── try 1: coin_change(2)
│   │   │   │   ├── try 1: coin_change(1) ⭐
│   │   │   │   │   ├── try 1: coin_change(0) ⭐ → 0
│   │   │   │   │   └── try 5: coin_change(-4) ⭐ → impossible
│   │   │   │   └── try 5: coin_change(-3) → impossible
│   │   │   └── try 5: coin_change(-2) → impossible
│   │   └── try 5: coin_change(-1) → impossible
│   └── try 5: coin_change(0) ⭐ → 0
└── try 5: coin_change(1) ⭐
    ├── try 1: coin_change(0) ⭐ → 0
    └── try 5: coin_change(-4) ⭐ → impossible
```

## Verification Against AI's Explanation

### What the AI said about repeated subproblems

It said that different first-coin choices converge on identical remaining
amounts, causing an entire subtree to be rebuilt each time because the
function stores no previous answers.

### What I found in my manual trace

- `coin_change(0)` appears 3 times.
- `coin_change(1)` appears 2 times.
- `coin_change(5)` appears 1 time.

### Did the AI's explanation match my trace?

Yes. Amounts 1 and 0 recur exactly as predicted, and each repeated amount has
the same descendants and result every time.

### Something the AI identified that I had not noticed

The amount itself is sufficient as the memoisation key only because every
recursive call retains the same unlimited denomination list. No record of the
coin-choice path is needed to identify a subproblem.

### Something I found that the AI's explanation did not fully cover

Negative terminal states repeat too: `coin_change(-4)` appears twice in this
small tree. They are cheap base cases, but they still contribute to the call
count and make the exact tree larger than a trace of only nonnegative amounts.

## Targeted Benchmark

| amount | calls | time (s) |
|---:|---:|---:|
| 10 | 101 | 0.0000 |
| 20 | 2,221 | 0.0004 |
| 30 | 47,325 | 0.0081 |
| 40 | 1,010,369 | 0.1720 |
| 50 | 21,575,601 | 3.7420 |

Amount 50 was the practical stopping point. The benchmark remained correct,
but going higher would multiply already noticeable runtime without adding a
new conclusion.

## AI's Preview of the Fix

### What the AI says needs to be stored

Store a mapping from each remaining amount to the minimum number of coins
already calculated for it. Before branching, return the cached result when it
exists; after calculating a new amount, store the answer once. Impossible
states may also be cached as `math.inf`.

### How many unique subproblems exist for this problem

For target amount A, there are A + 1 meaningful nonnegative states—amounts 0
through A. A fixed largest coin can also produce only a constant-width band of
negative base cases, so the total number of distinct states remains Θ(A).

### My understanding of why that number of subproblems matters

Memoisation collapses an exponential recursion tree into one calculation per
amount. Each state tries c denominations, producing O(A × c) time and O(A)
stored results. With `[1, 5, 10, 25]`, c is four and the time simplifies to
O(A).

## Reflection

My hypothesis was correct: the smallest nonnegative states, especially amounts
1 and 0, recur most often because many coin-choice sequences eventually
converge there. The decreasing-amount structure suggested this before the
trace, although I had not initially considered repeated negative base cases.

I first saw repetition when the right branch from amount 6 reached amount 1,
which had already appeared deep inside the left branch. I could predict some
convergence from the recurrence, but drawing the tree made both the duplicate
subtree and the repeated terminal calls concrete.

Writing the naive solution first made the AI conversation more precise than a
code-generation-first lab. I could ask about a recurrence I already
understood, challenge its complexity bound against actual counters, and verify
its explanation node by node instead of evaluating unfamiliar generated code.
