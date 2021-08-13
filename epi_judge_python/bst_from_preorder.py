from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:

    root_index = 0
    def helper(L, U):
        nonlocal root_index
        if root_index == len(preorder_sequence):
            return None
        root = preorder_sequence[root_index]
        if not L <= root <= U:
            return None
        root_index += 1
        left = helper(L, root)
        right = helper(root, U)
        return BstNode(root, left, right)
    return helper(float('-inf'), float('inf'))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
