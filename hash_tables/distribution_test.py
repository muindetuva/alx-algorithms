#!/usr/bin/python3
"""Measure normal and adversarial hash-function distributions."""

import math

from hash_function import adversarial_keys, custom_hash, improved_hash


def measure_distribution(keys, num_buckets):
    """Return distribution measurements for custom_hash over keys."""
    bucket_counts = [0] * num_buckets

    for key in keys:
        index = custom_hash(key, num_buckets)
        bucket_counts[index] += 1

    collided_buckets = sum(1 for count in bucket_counts if count > 1)
    collision_rate = collided_buckets / num_buckets
    max_chain = max(bucket_counts)
    mean = len(keys) / num_buckets
    variance = sum(
        (count - mean) ** 2 for count in bucket_counts
    ) / num_buckets
    std_dev = math.sqrt(variance)

    return {
        "bucket_counts": bucket_counts,
        "collision_rate": round(collision_rate, 3),
        "max_chain": max_chain,
        "std_dev": round(std_dev, 3),
        "empty_buckets": bucket_counts.count(0),
    }


def print_distribution_report(label, keys, num_buckets):
    """Print and return a readable distribution report."""
    results = measure_distribution(keys, num_buckets)
    load = len(keys) / num_buckets
    print(f"\n{'=' * 50}")
    print(f"Test: {label}")
    print(f"Keys: {len(keys)} | Buckets: {num_buckets} | Load: {load:.2f}")
    print(f"Max chain length: {results['max_chain']}")
    print(f"Empty buckets: {results['empty_buckets']}")
    print(f"Collision rate: {results['collision_rate']}")
    print(f"Std deviation: {results['std_dev']} (lower = more uniform)")
    print(f"{'=' * 50}")
    return results


def measure_improved(keys, num_buckets):
    """Print and return improved_hash measurements over keys."""
    bucket_counts = [0] * num_buckets
    for key in keys:
        index = improved_hash(key, num_buckets)
        bucket_counts[index] += 1

    max_chain = max(bucket_counts)
    mean = len(keys) / num_buckets
    variance = sum(
        (count - mean) ** 2 for count in bucket_counts
    ) / num_buckets
    std_dev = math.sqrt(variance)
    results = {
        "bucket_counts": bucket_counts,
        "max_chain": max_chain,
        "std_dev": round(std_dev, 3),
        "empty_buckets": bucket_counts.count(0),
    }
    print("\nImproved function on adversarial keys:")
    print(f"Max chain: {max_chain} | Std dev: {results['std_dev']}")
    return results


def run_tests():
    """Run the seven distribution experiments from the lab."""
    random_keys = [
        "xK9mP2", "rL4nQ7", "bW3vT8", "jH6sU1", "dF5yA0",
        "eM8cR3", "gN2oI6", "hJ1pB9", "kC7qE4", "lD0wX5",
        "mZ9aG2", "nY8bH7", "oX7cJ4", "pW6dK1", "qV5eL8",
        "rU4fM3", "sT3gN0", "tS2hO9", "uR1iP6", "vQ0jQ5",
    ]
    sequential_keys = [str(number) for number in range(100)]
    english_words = [
        "the", "be", "to", "of", "and", "a", "in", "that", "have",
        "it", "for", "not", "on", "with", "he", "as", "you", "do",
        "at", "this", "but", "his", "by", "from", "they", "we",
        "say", "her", "she", "or", "an", "will", "my", "one", "all",
        "would", "there", "their", "what",
    ]
    similar_keys = [f"user_{number:04d}" for number in range(50)]
    single_char_keys = [chr(number) for number in range(32, 127)]

    reports = {
        "random": print_distribution_report(
            "Random-looking keys", random_keys, 16
        ),
        "sequential": print_distribution_report(
            "Sequential numeric strings", sequential_keys, 16
        ),
        "english": print_distribution_report(
            "Common English words", english_words, 16
        ),
        "similar": print_distribution_report(
            "Similar strings (user_0000 to user_0049)", similar_keys, 16
        ),
        "single": print_distribution_report(
            "Single ASCII characters", single_char_keys, 16
        ),
    }

    adversarial = print_distribution_report(
        "AI-designed adversarial inputs", adversarial_keys, 16
    )
    collided = sum(
        1 for count in adversarial["bucket_counts"] if count > 1
    )
    print(f"Buckets containing collisions: {collided}")
    reports["adversarial"] = adversarial
    reports["improved"] = measure_improved(adversarial_keys, 16)
    return reports


if __name__ == "__main__":
    run_tests()
