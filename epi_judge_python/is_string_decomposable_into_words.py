import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from functools import lru_cache
from collections import deque

def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:

    @lru_cache(maxsize=None)
    def decompose(end_index, prefix):
        if end_index == len(domain)-1:
            return deque([prefix]) if prefix in dictionary else None

        with_prefix = decompose(end_index+1, prefix+domain[end_index+1])
        if prefix in dictionary:
            if with_prefix is not None:
                return with_prefix
            else:
                chunked = decompose(end_index+1, domain[end_index+1])
                if chunked is not None:
                    chunked.appendleft(prefix)
                return chunked
        else:
            return with_prefix
    # D(0, 'b') => D(1, 'be') => D(2, 'bed')
    #                               => D(3, 'bedb') => ... => D(len(domain)-1, 'bedbathandbeyond')
    #                               => D(3, 'b') => D(4, 'ba') => D(5, 'bat')
            #                                                               => D(6, 'bath')
    #                                                                       => D(6, 'h') => ...
    #
    #   => D(10, 'b') => ... D(15, 'beyond') *
    #   => D(10, 'b') *
    res = decompose(0, domain[0])
    res = list(res) if res is not None else []
    return res

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
