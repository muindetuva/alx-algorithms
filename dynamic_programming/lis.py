#!/usr/bin/python3
"""Top-down and bottom-up dynamic programming solutions for LIS."""


# -- Memoised (top-down) --

call_count = 0


def lis(nums, i, cache):
    """Return the LIS length ending at i using an explicit cache."""
    global call_count
    call_count += 1

    if i in cache:
        return cache[i]

    best = 1
    for previous in range(i):
        if nums[previous] < nums[i]:
            best = max(best, lis(nums, previous, cache) + 1)

    cache[i] = best
    return best


def longest_increasing_subsequence_memo(nums):
    """Return the LIS length using shared top-down memoisation."""
    if not nums:
        return 0

    cache = {}
    return max(lis(nums, index, cache) for index in range(len(nums)))


def longest_increasing_subsequence(nums):
    """Provide the wrapper name requested in the memoisation task."""
    return longest_increasing_subsequence_memo(nums)


# -- Tabulated (bottom-up) --


def lis_tabulation(nums):
    """Return the LIS length using a left-to-right DP table."""
    if not nums:
        return 0

    dp = [1] * len(nums)
    for index in range(len(nums)):
        for previous in range(index):
            if nums[previous] < nums[index]:
                dp[index] = max(dp[index], dp[previous] + 1)

    return max(dp)


# -- Tests --


if __name__ == "__main__":
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
        ([5, 5, 5, 5, 5], 1),
        ([1], 1),
        ([], 0),
    ]

    for numbers, expected in test_cases:
        call_count = 0
        memo_result = longest_increasing_subsequence_memo(numbers)
        calls = call_count
        tab_result = lis_tabulation(numbers)
        memo_status = "PASS" if memo_result == expected else "FAIL"
        tab_status = "PASS" if tab_result == expected else "FAIL"
        print(
            f"Memo {memo_status} Tab {tab_status} | LIS({numbers}) = "
            f"{memo_result}/{tab_result} (expected {expected}) | "
            f"memo calls: {calls}"
        )
