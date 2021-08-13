from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    result = []
    def largest(node: BstNode, remaining):
        if node is None:
            return remaining
        if remaining > 0:
            R = largest(node.right, remaining)
            if R > 0:
                result.append(node.data)
                return largest(node.left, R-1)
            else:
                return R
        return remaining

    largest(tree, k)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
