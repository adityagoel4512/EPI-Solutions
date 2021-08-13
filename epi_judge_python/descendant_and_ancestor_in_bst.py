import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:
    def try_find_path(cur_node, target):
        if cur_node is None:
            return False
        elif cur_node is target:
            return True

        if target is None:
            return try_find_path(cur_node.left, None)
        elif cur_node.data > target.data:
            return try_find_path(cur_node.left, target)
        else:
            return try_find_path(cur_node.right, target)

    if possible_anc_or_desc_0 is middle or middle is possible_anc_or_desc_1:
        return False

    path_to_middle_0 = try_find_path(possible_anc_or_desc_0, middle)
    if path_to_middle_0:
        return try_find_path(middle, possible_anc_or_desc_1)
    else:
        return try_find_path(possible_anc_or_desc_1, middle) and try_find_path(middle, possible_anc_or_desc_0)

@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
