# Prompt Log — AI Lab 10

## Prompt 1 — Predict Each Shape

**Prompt used:**

> I am going to insert seven values into an initially empty binary search tree,
> using the standard BST insertion rule (left if smaller, right if larger). For
> each of the three insertion orders below, predict the shape of the resulting
> tree, state its height, and state the worst-case number of comparisons to
> search for a value. Show your reasoning step by step for each insertion—do
> not just give me the final answer.
>
> Sequence A: 50, 25, 75, 10, 40, 60, 90
> Sequence B: 10, 25, 40, 50, 60, 75, 90
> Sequence C: 10, 90, 25, 75, 40, 60, 50

**Why this prompt was structured this way:**

I requested every insertion step so the predicted shape could be audited
instead of accepting only three final heights.

## Prompt 2 — Probe the Worst Case

**Prompt used:**

> Sequence B is inserted in ascending order. Explain exactly why that produces
> the shape it does, and what data structure the resulting tree is effectively
> equivalent to. What is its search complexity in Big-O terms, and how does
> that compare to Sequence A?

**Why this prompt was structured this way:**

It forces the shape prediction to connect to an equivalent linear structure
and a concrete complexity consequence.

## Prompt 3 — Challenge with a Tricky Detail

**Prompt used:**

> For Sequence C, walk me through the insertion of the value 50 specifically—
> it is inserted last. Which existing nodes does it get compared against on the
> way down, and where does it end up? Does your earlier sketch of Sequence C
> place it correctly?

**Why this prompt was structured this way:**

The last insertion exposes whether AI simulated the zig-zag path or guessed
from the words "mixed order."

## Prompt 4 — Verification Script

**Prompt used:**

> Write me a Python program that defines a BST with an insert method, builds all
> three trees from the sequences above, and for each one prints (a) its height
> and (b) the worst-case search cost. Include a function that computes the
> height of a tree so I can verify your predictions rather than trusting them.

**Why this prompt was structured this way:**

It requests independent measurements for the two claims under review and a
repeatable implementation against which to compare both prediction sets.

## What I would change about these prompts next time

I would define height as node levels in the first prompt and request an in-order
traversal immediately, eliminating convention ambiguity and adding a second
structural check from the beginning.
