#!/usr/bin/python3
"""Benchmark five sorting approaches on five 10,000-item datasets."""

import random
import statistics
import timeit

from sorting import bubble_sort, insertion_sort, merge_sort, quicksort


DATASET_SIZE = 10_000
SEED = 2026


def generate_datasets():
    """Return the five reproducible datasets required by the lab."""
    generator = random.Random(SEED)
    random_values = [
        generator.randint(0, DATASET_SIZE * 10)
        for _ in range(DATASET_SIZE)
    ]
    ascending = list(range(DATASET_SIZE))
    descending = list(range(DATASET_SIZE - 1, -1, -1))
    nearly_sorted = ascending.copy()
    for _ in range(100):
        first, second = generator.sample(range(DATASET_SIZE), 2)
        nearly_sorted[first], nearly_sorted[second] = (
            nearly_sorted[second],
            nearly_sorted[first],
        )

    high_duplicates = [42] * 9_000
    other_values = [value for value in range(100) if value != 42]
    high_duplicates.extend(
        generator.choice(other_values)
        for _ in range(1_000)
    )
    generator.shuffle(high_duplicates)

    return {
        "A — Random": random_values,
        "B — Sorted ascending": ascending,
        "C — Sorted descending": descending,
        "D — Nearly sorted": nearly_sorted,
        "E — High duplicates": high_duplicates,
    }


ALGORITHMS = {
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Quicksort": quicksort,
    "Timsort": sorted,
}

REPETITIONS = {
    "Bubble": 1,
    "Insertion": 1,
    "Merge": 3,
    "Quicksort": 3,
    "Timsort": 3,
}


def benchmark_algorithm(algorithm, data, repetitions):
    """Return the median runtime for one algorithm and dataset."""
    timings = timeit.repeat(
        lambda: algorithm(data),
        repeat=repetitions,
        number=1,
    )
    return statistics.median(timings)


def run_benchmark():
    """Run every algorithm on every dataset and print a results table."""
    datasets = generate_datasets()
    results = {}
    print(f"Dataset size: {DATASET_SIZE:,} elements")
    print("Quadratic sorts: 1 run; other algorithms: median of 3 runs.\n")

    for dataset_name, data in datasets.items():
        dataset_results = {}
        expected = sorted(data)
        for algorithm_name, algorithm in ALGORITHMS.items():
            output = algorithm(data)
            if output != expected:
                raise AssertionError(f"{algorithm_name} produced wrong output")
            elapsed = benchmark_algorithm(
                algorithm,
                data,
                REPETITIONS[algorithm_name],
            )
            dataset_results[algorithm_name] = elapsed

        results[dataset_name] = dataset_results
        ranked = sorted(dataset_results.items(), key=lambda item: item[1])
        print(f"{dataset_name}")
        print("Algorithm    Time (s)    Rank")
        print("-----------  ----------  ----")
        for rank, (algorithm_name, elapsed) in enumerate(ranked, start=1):
            print(f"{algorithm_name:<11}  {elapsed:>10.6f}  {rank:>4}")
        print(f"Fastest: {ranked[0][0]} | Slowest: {ranked[-1][0]}\n")

    return results


if __name__ == "__main__":
    run_benchmark()
