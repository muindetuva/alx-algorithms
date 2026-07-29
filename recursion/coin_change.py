#!/usr/bin/python3
"""Measure repeated work in naive recursive minimum coin change."""

import math
import timeit


call_count = 0


def coin_change_naive(coins, amount):
    """Return the fewest coins for amount using un-memoised recursion."""
    global call_count
    call_count += 1

    if amount == 0:
        return 0
    if amount < 0:
        return math.inf

    best_smaller_solution = min(
        coin_change_naive(coins, amount - coin)
        for coin in coins
    )
    return 1 + best_smaller_solution


def run_examples():
    """Run the required correctness examples and larger call-count cases."""
    global call_count
    coins = [1, 5, 10, 25]
    tests = [
        (6, 2),
        (11, 2),
        (36, 3),
        (41, 4),
    ]

    for amount, expected in tests:
        call_count = 0
        result = coin_change_naive(coins, amount)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"{status} coin_change({amount}) = {result} "
            f"(expected {expected}) | calls: {call_count:,}"
        )

    for amount in [20, 30, 40, 50]:
        call_count = 0
        result = coin_change_naive(coins, amount)
        print(f"coin_change({amount}) = {result} | calls: {call_count:,}")


def run_benchmark():
    """Time selected amounts and recount each run for a clear table."""
    global call_count
    coins = [1, 5, 10, 25]
    amounts = [10, 20, 30, 40, 50]

    print(f"\n{'amount':<10} {'calls':>12} {'time (s)':>12}")
    print("-" * 36)

    for amount in amounts:
        call_count = 0
        elapsed = timeit.timeit(
            lambda: coin_change_naive(coins, amount),
            number=1,
        )
        call_count = 0
        coin_change_naive(coins, amount)
        print(f"{amount:<10} {call_count:>12,} {elapsed:>12.4f}")


if __name__ == "__main__":
    run_examples()
    run_benchmark()
