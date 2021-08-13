from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    A_set = set(A)
    max_range = 0
    for v in A:
        U = v
        while U in A_set:
            A_set.discard(U)
            U += 1
        D = v-1
        while D in A_set:
            A_set.discard(D)
            D -= 1
        max_range = max(max_range, U-D-1)

    return max_range


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
