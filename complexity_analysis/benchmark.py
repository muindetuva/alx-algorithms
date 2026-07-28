import random
import timeit

from solutions import find_duplicates_a, find_duplicates_b


TOTAL_RECORDS = 10_000
DUPLICATE_RATIO = 0.20
REPEATS = 3


def make_records(total=TOTAL_RECORDS, duplicate_ratio=DUPLICATE_RATIO):
    """Build a deterministic data set with the requested duplicate ratio."""
    duplicate_count = int(total * duplicate_ratio)
    unique_count = total - duplicate_count
    records = list(range(100_000, 100_000 + unique_count))
    generator = random.Random(42)
    records.extend(generator.sample(records, duplicate_count))
    generator.shuffle(records)
    return records


def measure(function, records):
    """Return the fastest of several one-run measurements."""
    timings = timeit.repeat(
        lambda: function(records),
        repeat=REPEATS,
        number=1,
    )
    return min(timings)


def main():
    records = make_records()
    duplicates_a = find_duplicates_a(records)
    duplicates_b = find_duplicates_b(records)

    if set(duplicates_a) != set(duplicates_b):
        raise RuntimeError("The two solutions returned different duplicates")

    time_a = measure(find_duplicates_a, records)
    time_b = measure(find_duplicates_b, records)
    ratio = time_a / time_b

    print(f"Benchmark: {len(records):,} records, 20% duplicates")
    print(f"Solution A: {time_a:.6f} seconds")
    print(f"Solution B: {time_b:.6f} seconds")
    print(f"Solution B is approximately {ratio:.1f}x faster")


if __name__ == "__main__":
    main()
