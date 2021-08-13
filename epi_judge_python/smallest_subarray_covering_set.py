import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

from collections import Counter
def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    remaining_to_cover = len(keywords)
    keywords_covered = {keyword:0 for keyword in keywords}
    L = 0
    result = None
    def update_result(i, j):
        d_new = j - i
        if result is None or d_new < result.end-result.start:
            return Subarray(start=i, end=j)
        else:
            return result

    for R, word in enumerate(paragraph):
        if word in keywords:
            if keywords_covered[word] == 0:
                remaining_to_cover -= 1
            keywords_covered[word] += 1


        while remaining_to_cover == 0:
            result = update_result(L, R)
            if paragraph[L] in keywords:
                keywords_covered[paragraph[L]] -= 1
                if keywords_covered[paragraph[L]] == 0:
                    remaining_to_cover += 1
            L += 1
    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
