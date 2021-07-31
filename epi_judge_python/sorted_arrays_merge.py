from typing import List

from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    def generate_values():
        iters = list(map(iter, sorted_arrays))
        min_heap = []
        for i in range(len(sorted_arrays)):
            try:
                heapq.heappush(min_heap, (next(iters[i]), i))
            except StopIteration:
                continue

        while min_heap:
            min_elem, min_arr = heapq.heappop(min_heap)
            yield min_elem
            try:
                heapq.heappush(min_heap, (next(iters[min_arr]), min_arr))
            except StopIteration:
                continue

    return list(generate_values())

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
