#!/usr/bin/python3
"""Original and improved custom string hash functions."""


def _validate_inputs(key, num_buckets):
    """Reject values outside the public functions' documented contract."""
    if not isinstance(key, str):
        raise TypeError("key must be a string")
    if not isinstance(num_buckets, int) or num_buckets <= 0:
        raise ValueError("num_buckets must be a positive integer")


def custom_hash(key, num_buckets):
    """Hash a string with a base-31 polynomial rolling calculation."""
    _validate_inputs(key, num_buckets)
    hash_value = 0

    for character in key:
        hash_value = (hash_value * 31 + ord(character)) % num_buckets

    return hash_value


adversarial_keys = [
    "aa",
    "bb",
    "cc",
    "dd",
    "ee",
    "ff",
    "gg",
    "hh",
    "ii",
    "jj",
]


def improved_hash(key, num_buckets):
    """Hash a string with FNV-1a mixing and a 64-bit final avalanche."""
    _validate_inputs(key, num_buckets)
    hash_value = 14695981039346656037
    mask = 0xFFFFFFFFFFFFFFFF

    for character in key:
        hash_value ^= ord(character)
        hash_value = (hash_value * 1099511628211) & mask

    hash_value ^= hash_value >> 33
    hash_value = (hash_value * 0xFF51AFD7ED558CCD) & mask
    hash_value ^= hash_value >> 33
    hash_value = (hash_value * 0xC4CEB9FE1A85EC53) & mask
    hash_value ^= hash_value >> 33
    return hash_value % num_buckets
