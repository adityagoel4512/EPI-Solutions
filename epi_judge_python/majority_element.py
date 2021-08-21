from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    candidate = next(stream)
    candidate_count = 1
    for it in stream:
        if it == candidate:
            candidate_count += 1
        else: # it != candidate:
            candidate_count -= 1
            if candidate_count == 0:
                candidate = it
                candidate_count = 1
    return candidate

def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
