# SE03 — AI Lab 01: Complexity Analysis

## What this repository is about

This directory is the deliverable for AI Lab 1 of the SE-03 Algorithmic Thinking course. It contains two Python solutions to a duplicate-detection problem, a benchmark comparing their real-world performance, and a documented analysis of the time and space complexity of each — produced by interrogating an AI tool and critically evaluating its reasoning.

## Repository contents

| File | Description |
|---|---|
| `solutions.py` | The two solutions being compared |
| `benchmark.py` | Benchmarking script generated with AI, verified, and run |
| `my_analysis.md` | Complexity analysis before and after AI interrogation |
| `prompts.md` | Exact prompts used and the reasoning behind each one |
| `README.md` | Project overview, contents, findings, and recommendation |

## Key findings

- **Solution A complexity:** O(n²) pair comparisons with an O(d) list-membership check inside them, producing a loose O(n³) worst-case upper bound; O(n) worst-case auxiliary space.
- **Solution B complexity:** O(n) average time and O(n) auxiliary space.
- **Benchmark result at n=10,000:** Solution A took 1.280584 seconds and Solution B took 0.000358 seconds, making B approximately 3,572.1 times faster in this run.
- **Recommendation:** Use Solution B in production because its linear average-time approach scales far better, with reasonable memory as the tradeoff.

## Run the files

```bash
python3 solutions.py
python3 benchmark.py
```

The benchmark uses a deterministic set of 10,000 records with approximately 20% duplicates and reports the fastest of three runs for each solution. Exact timings vary by machine.

## AI tool used

OpenAI Codex was used as the AI thinking partner. Its first analysis was challenged, its benchmark was reviewed before execution, and the final conclusions were checked against both the code and measured results.
