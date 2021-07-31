from typing import List

from test_framework import generic_test, test_utils

def take(k, g):
    it = iter(g)
    for _ in range(k):
        try:
            yield next(it)
        except StopIteration:
            return

import heapq
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:

    def get_largest_from_candidates():
        candidates_max_heap = [(-A[0], 0)]
        while candidates_max_heap:
            max_val, max_index = heapq.heappop(candidates_max_heap)
            yield -max_val
            # add children
            L = 2*max_index+1
            R = 2*max_index+2
            if L < len(A):
                heapq.heappush(candidates_max_heap, (-A[L], L))
            if R < len(A):
                heapq.heappush(candidates_max_heap, (-A[R], R))
    return list(take(k, get_largest_from_candidates()))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
