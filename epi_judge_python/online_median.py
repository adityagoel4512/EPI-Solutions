from typing import Iterator, List

from test_framework import generic_test

import heapq
def online_median(sequence: Iterator[int]) -> List[float]:

    def generate_medians():
        max_heap = []
        min_heap = []

        for x in sequence:
            if not max_heap:
                heapq.heappush(max_heap, -x)
            elif x <= -max_heap[0]:
                heapq.heappush(max_heap, -x)
            elif x > -max_heap[0]:
                heapq.heappush(min_heap, x)

            diff = len(max_heap) - len(min_heap)

            if diff == 2:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif diff == -2:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))


            diff = len(max_heap) - len(min_heap)

            if diff == 1:
                yield -max_heap[0]
            elif diff == 0:
                yield (-max_heap[0] + min_heap[0])/2.0
            elif diff == -1:
                yield min_heap[0]


    return list(generate_medians())

def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
