from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def helper(node, prefix=0):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return prefix * 2 + node.data
        total = helper(node.left, (prefix * 2) + node.data)
        total += helper(node.right, (prefix * 2) + node.data)
        return total
    return helper(tree)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
