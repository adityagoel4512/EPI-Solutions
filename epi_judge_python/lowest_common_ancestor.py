import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def helper(node):
        if node is None:
            return False, False, None

        if node is node0 and node0 is node1:
            return True, True, node

        l = helper(node.left)
        r = helper(node.right)

        if node is node0:
            if l[1] or r[1]:
                return True, True, node
            else:
                return True, False, None

        if node is node1:
            if l[0] or r[0]:
                return True, True, node
            else:
                return False, True, node

        if (l[0] and r[1]) or (l[1] and r[0]):
            return True, True, node

        if l[0] and l[1]:
            return l

        if r[0] and r[1]:
            return r

        return l[0] or r[0], l[1] or r[1], None

    res = helper(tree)
    return res[2]

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
