from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def is_balanced(tree):
        if tree is None:
            return (0, True)
        (hl, lb) = is_balanced(tree.left)
        if not lb:
            return (-1, lb)
        (hr, rb) = is_balanced(tree.right)
        if not rb:
            return (-1, rb)
        return (max(hl, hr)+1, abs(hl-hr) <= 1)

    return is_balanced(tree)[1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
