from typing import List

from test_framework import generic_test


def calculate_largest_rectangle(heights: List[int]) -> int:
    # rect(i, j) = (j-i) * min(heights[k] for k in range(i, j+1))
    # 1. increase width 2. increase the minimum building height in the range
    # if heights[i] < heights[j] => i += 1
    result = 0
    for i, height in enumerate(heights):
        L = i
        while L >= 0 and heights[L] >= height:
            L -= 1
        R = i
        while R < len(heights) and heights[R] >= height:
            R += 1
        width = R-L-1
        result = max(result, width * height)
    return result
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
