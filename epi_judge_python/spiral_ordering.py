from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []
    N = len(square_matrix)
    for i in range(0, N//2):
        result.extend(square_matrix[i][c] for c in range(i, N-i))
        result.extend(square_matrix[r][N-i-1] for r in range(i+1, N-i))
        result.extend(square_matrix[N-i-1][c] for c in range(N-i-2, i, -1))
        result.extend(square_matrix[r][i] for r in range(N-i-1, i, -1))
    if N & 1:
        result.append(square_matrix[N//2][N//2])
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
