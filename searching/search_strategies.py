#!/usr/bin/python3
"""Linear, cached binary, and cached hash-set search strategies."""

from bisect import bisect_left


_binary_source = None
_sorted_catalogue = None
_hash_source = None
_catalogue_set = None


def reset_caches():
    """Clear prepared structures so setup costs can be measured fairly."""
    global _binary_source, _sorted_catalogue
    global _hash_source, _catalogue_set
    _binary_source = None
    _sorted_catalogue = None
    _hash_source = None
    _catalogue_set = None


def linear_search(catalogue, target):
    """Return whether target appears using a plain left-to-right scan."""
    for product_id in catalogue:
        if product_id == target:
            return True
    return False


def binary_search_approach(catalogue, target):
    """Sort once per catalogue object, then search it with bisect_left."""
    global _binary_source, _sorted_catalogue
    if catalogue is not _binary_source:
        _sorted_catalogue = sorted(catalogue)
        _binary_source = catalogue

    position = bisect_left(_sorted_catalogue, target)
    return (
        position < len(_sorted_catalogue)
        and _sorted_catalogue[position] == target
    )


def hash_search_approach(catalogue, target):
    """Build one set per catalogue object, then use set membership."""
    global _hash_source, _catalogue_set
    if catalogue is not _hash_source:
        _catalogue_set = set(catalogue)
        _hash_source = catalogue
    return target in _catalogue_set
