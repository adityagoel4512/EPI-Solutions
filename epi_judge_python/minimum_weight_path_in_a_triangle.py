from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    min_path_weights = [0]
    for row in triangle:
        row_path = []
        for i, val in enumerate(row):
            if i == 0:
                row_path.append(min_path_weights[i] + val)
            elif i == len(row)-1:
                row_path.append(min_path_weights[-1]+val)
            else:
                row_path.append(min(min_path_weights[i], min_path_weights[i-1])+val)
        min_path_weights = row_path

    return min(min_path_weights)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
