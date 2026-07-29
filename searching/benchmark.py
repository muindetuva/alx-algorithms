#!/usr/bin/python3
"""Benchmark setup and search costs for three catalogue strategies."""

import timeit

from products import catalogue, targets
from search_strategies import (
    binary_search_approach,
    hash_search_approach,
    linear_search,
    reset_caches,
)


RUNS = 1_000
STRATEGIES = {
    "Linear": linear_search,
    "Sort + binary": binary_search_approach,
    "Hash set": hash_search_approach,
}


def measure_first_call(strategy, target):
    """Time one cold-cache call that includes any setup work."""
    reset_caches()
    return timeit.timeit(lambda: strategy(catalogue, target), number=1)


def measure_search(strategy, target):
    """Return average warmed search time over RUNS calls."""
    strategy(catalogue, target)
    total = timeit.timeit(
        lambda: strategy(catalogue, target),
        number=RUNS,
    )
    return total / RUNS


def run_benchmark():
    """Measure all strategies and print setup, search, and total tables."""
    setup_times = {"Linear": 0.0}
    search_times = {name: {} for name in STRATEGIES}
    first_target = targets["present_early"]

    for name in ("Sort + binary", "Hash set"):
        strategy = STRATEGIES[name]
        first_call = measure_first_call(strategy, first_target)
        warm_search = measure_search(strategy, first_target)
        setup_times[name] = max(0.0, first_call - warm_search)

    for name, strategy in STRATEGIES.items():
        reset_caches()
        strategy(catalogue, first_target)
        for target_name, target in targets.items():
            search_times[name][target_name] = measure_search(strategy, target)

    total_times = {}
    for name in STRATEGIES:
        search_total = sum(search_times[name].values()) * RUNS
        total_times[name] = setup_times[name] + search_total

    print(f"Catalogue: {len(catalogue):,} IDs | Runs per target: {RUNS:,}\n")
    print("Setup times")
    print("Approach         Time (s)")
    print("---------------  ----------")
    for name in STRATEGIES:
        print(f"{name:<15}  {setup_times[name]:>10.8f}")

    print("\nAverage search time per call")
    header = "Target          Linear       Binary       Hash"
    print(header)
    print("-" * len(header))
    for target_name in targets:
        print(
            f"{target_name:<14}  "
            f"{search_times['Linear'][target_name]:>10.8f}  "
            f"{search_times['Sort + binary'][target_name]:>10.8f}  "
            f"{search_times['Hash set'][target_name]:>10.8f}"
        )

    print("\nTotal time: setup + four targets × 1,000 searches")
    print("Approach         Total (s)   Relative to hash")
    print("---------------  ----------  ----------------")
    hash_total = total_times["Hash set"]
    for name in STRATEGIES:
        relative = total_times[name] / hash_total
        print(f"{name:<15}  {total_times[name]:>10.8f}  {relative:>15.2f}x")

    return {
        "setup_times": setup_times,
        "search_times": search_times,
        "total_times": total_times,
    }


if __name__ == "__main__":
    run_benchmark()
