from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    cur_subarray = 0
    max_subarray = 0
    for a in A:
        cur_subarray = max(a+cur_subarray, a)
        max_subarray = max(max_subarray, cur_subarray)
    return max_subarray

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
