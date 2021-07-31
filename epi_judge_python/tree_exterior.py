import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    def left_exterior(node):
        if node.left or node.right:
            result.append(node)
        if node.left:
            left_exterior(node.left)
        elif node.right:
            left_exterior(node.right)


    def right_exterior(node):
        if node.right:
            right_exterior(node.right)
        elif node.left:
            right_exterior(node.left)

        if node.left or node.right:
            # not a leaf
            result.append(node)

    def bottom_exterior(node):

        if node is None:
            return
        if node.left is None and node.right is None:
            result.append(node)
            return
        bottom_exterior(node.left)
        bottom_exterior(node.right)

    if tree is None:
        return []
    result = [tree]
    if tree.left:
        left_exterior(tree.left)
        bottom_exterior(tree.left)
    if tree.right:
        bottom_exterior(tree.right)
        right_exterior(tree.right)

    return result

def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
