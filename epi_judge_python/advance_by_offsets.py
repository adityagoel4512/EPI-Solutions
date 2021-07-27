from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    max_reach = 0
    i = 0
    while i <= max_reach and max_reach < len(A)-1:
        max_reach = max(max_reach, A[i] + i)
        i += 1
    return max_reach >= len(A)-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
