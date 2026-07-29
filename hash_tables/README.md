# SE03 — AI Lab 05: Hash Function Design and Stress-Testing

## What this repository is about

This directory is the deliverable for AI Lab 5 of the SE-03 Algorithmic
Thinking course. An AI tool was asked to design a custom hash function. The
function was then stress-tested across five different input categories,
attacked with adversarial inputs designed to maximise collisions, and improved
based on the findings.

## Repository contents

| File | Description |
|---|---|
| `hash_function.py` | Original hash, adversarial keys, and improved hash |
| `distribution_test.py` | Seven distribution tests across input types |
| `hash_analysis.md` | Hypotheses, results, attacks, and comparison |

## Key findings

### Original function

- **Best performance on:** Single ASCII characters, with standard deviation
  0.242.
- **Worst performance on:** Adversarial repeated-character pairs, with
  standard deviation 2.421 and 15 empty buckets.
- **Weakness found:** With 16 buckets, multiplier 31 behaves like -1, so
  two-character keys with equal character values all map to bucket 0.

### Adversarial inputs

- **Collision achieved:** Yes—all 10 keys mapped to the same bucket.
- **Max chain length on adversarial inputs:** 10

### Improved function

- **What was changed:** FNV-1a multiplication and XOR mixing were followed by
  a 64-bit avalanche before reducing the result to a bucket index.
- **Max chain length on adversarial inputs after fix:** 3
- **Improvement:** The longest chain fell by 70%, from 10 to 3.

## Running the project

```bash
python3 distribution_test.py
```

## AI tool used

OpenAI Codex was used to design, attack, and improve the functions.
