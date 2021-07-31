from typing import List

from test_framework import generic_test

import heapq
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:

    cmps = [lambda x, y: x <= y, lambda x, y: x >= y]
    def get_section(start, ascending):
        i = start+1
        while i < len(A) and cmps[ascending](A[i], A[i-1]):
            i += 1
        return A[start:i] if ascending else list(reversed(A[start:i])), i

    i = 0
    ascending = True
    sections = []
    while i < len(A):
        section, i = get_section(i, ascending)
        ascending = not ascending
        sections.append(section)

    return list(heapq.merge(*sections))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
