import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))
def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    keyword_to_prev = dict(zip(keywords[1:], keywords))
    keyword_subarray = {keyword:(None, None) for keyword in keywords}
    # maintains for each keyword the last index it was at and the longest complete subarray
    # length, complete meaning that it contains all preceding keywords

    result = None
    for i, word in enumerate(paragraph):
        if word == keywords[0]:
            keyword_subarray[word] = (i, 1)
        elif word in keyword_to_prev:
            prev_index, prev_length = keyword_subarray[keyword_to_prev[word]]
            if prev_length is not None:
                keyword_subarray[word] = (i, i-prev_index+prev_length)
                if word == keywords[-1]:
                    result = Subarray(i-keyword_subarray[word][1]+1, i) if result is None or keyword_subarray[word][1] < result.end-result.start+1 else result
    return result


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
