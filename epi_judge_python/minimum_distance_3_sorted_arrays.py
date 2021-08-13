from typing import List

from test_framework import generic_test
import heapq
def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]) -> int:
    min_heap = []
    max_value = float('-inf')
    for i, arr in enumerate(sorted_arrays):
        it = iter(arr)
        val = next(it, None)
        if val is not None:
            max_value = max(max_value, val)
            min_heap.append((val, i, it))

    heapq.heapify(min_heap)
    result = float('inf')
    while True:
        min_val, min_idx, min_iter = min_heap[0]
        result = min(max_value - min_val, result)
        next_val = next(min_iter, None)
        if next_val is None:
            return result
        max_value = max(max_value, next_val)
        heapq.heapreplace(min_heap, (next_val, min_idx, min_iter))
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
