#!/usr/bin/python3
"""Non-mutating implementations of four sorting algorithms."""

import random


def bubble_sort(values):
    """Return a bubble-sorted copy, stopping after a swap-free pass."""
    items = list(values)

    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = (
                    items[index + 1],
                    items[index],
                )
                swapped = True
        if not swapped:
            break

    return items


def insertion_sort(values):
    """Return an insertion-sorted copy of values."""
    items = list(values)

    for index in range(1, len(items)):
        current = items[index]
        position = index - 1
        while position >= 0 and items[position] > current:
            items[position + 1] = items[position]
            position -= 1
        items[position + 1] = current

    return items


def merge_sort(values):
    """Return a merge-sorted copy of values."""
    items = list(values)
    if len(items) <= 1:
        return items

    midpoint = len(items) // 2
    left = merge_sort(items[:midpoint])
    right = merge_sort(items[midpoint:])
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def quicksort(values):
    """Return a three-way quicksorted copy using a random pivot."""
    items = list(values)
    if len(items) <= 1:
        return items

    pivot = random.choice(items)
    lower = []
    equal = []
    higher = []

    for item in items:
        if item < pivot:
            lower.append(item)
        elif item > pivot:
            higher.append(item)
        else:
            equal.append(item)

    return quicksort(lower) + equal + quicksort(higher)
