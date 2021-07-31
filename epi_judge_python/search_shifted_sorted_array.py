from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    L = 0
    R = len(A)-1
    while L < R:
        M = (L+R)//2
        if A[M] < A[R]:
            R = M
        elif A[M] > A[R]:
            L = M+1
    return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
