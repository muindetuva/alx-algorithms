#!/usr/bin/python3
"""Reproducible product catalogue and search targets."""

import random


random.seed(42)

# Unsorted catalogue of 50,000 unique product IDs.
catalogue = random.sample(range(1, 500_001), 50_000)

# A mix of present and absent search values.
targets = {
    "present_early": catalogue[100],
    "present_middle": catalogue[25_000],
    "present_late": catalogue[49_000],
    "absent": 999_999,
}
