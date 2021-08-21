from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    # max(min(heights[i], heights[R]) * (j-i) for i in range(len(heights)) for j in range(i+1, len(heights)))
    # O(N^2)
    # n.b. we can improve a window's trapped water by either increasing the width or increasing the minimum height
    # if we have window i, R, then:
    # case 1: i is minimum, heights[i+1] > heights[i] => i += 1
    # case 2: R is minimum, heights[j-1] > heights[j] => j -= 1
    # case 3: i is the minimum, heights[i+1] <= heights[i] => R -= 1

    result = 0
    L = 0
    R = len(heights)-1
    while L < R:
        result = max(result, (min(heights[L], heights[R]) * (R - L)))
        if heights[L] <= heights[R]:
            L += 1
        else: # heights[L] > heights[R]
            R -= 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
