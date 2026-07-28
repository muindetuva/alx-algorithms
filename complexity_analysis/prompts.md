# Prompt Log — AI Lab 1

## Prompt 1 — Initial Analysis

**Prompt used:**

> I have two Python functions that solve the same problem: finding duplicate values in a list of product IDs. Both produce correct output. I want you to analyse them for time and space complexity.
>
> For each function:
>
> Identify what n is
>
> State the time complexity and explain your reasoning step by step
>
> State the space complexity and explain your reasoning
>
> Identify any potential performance issues at scale
>
> Do not tell me which is better yet. Just analyse each one independently first.

The two functions from `solutions.py` were pasted immediately after this prompt:

```python
def find_duplicates_a(records):
    duplicates = []
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            if records[i] == records[j]:
                if records[i] not in duplicates:
                    duplicates.append(records[i])
    return duplicates


def find_duplicates_b(records):
    seen = set()
    duplicates = set()
    for record in records:
        if record in seen:
            duplicates.add(record)
        else:
            seen.add(record)
    return list(duplicates)
```

**Why this prompt was structured this way:**

I requested independent analysis before a recommendation so the AI had to examine each implementation instead of jumping directly to a preference.

## Prompt 2 — Recommendation

**Prompt used:**

> Based on your analysis, which solution would you recommend for a production system that processes up to 1,000,000 records per day? Explain your recommendation in terms of the complexity difference and what that means in practice at that scale.

**Why this prompt was structured this way:**

I supplied a realistic scale and asked the AI to connect Big O notation to an engineering decision rather than merely naming the faster solution.

## Prompt 3 — Challenge

**Prompt used:**

> In Solution A, there is a line that reads if records[i] not in duplicates. What is the time complexity of that specific operation, and how does it affect the overall complexity of Solution A? Does your earlier analysis account for this?

**Why this prompt was structured this way:**

I isolated the list-membership operation to test whether the initial analysis had considered work inside the nested loops and to force a more precise worst-case explanation.

## Prompt 4 — Benchmark

**Prompt used:**

> Write me a Python script that benchmarks both solutions against each other using the timeit module. The benchmark should test both functions on a list of 10,000 records with approximately 20% duplicates. I want to see the actual time difference, not just the theoretical one.

**Why this prompt was structured this way:**

I specified the tool, input size, and duplicate ratio so the generated benchmark would be reproducible and would measure the scenario discussed in the analysis.

## What I would change about these prompts next time

Next time I would ask the AI to distinguish a loose upper bound from a tight bound immediately and require it to state its assumptions about duplicate distribution before recommending a solution.
