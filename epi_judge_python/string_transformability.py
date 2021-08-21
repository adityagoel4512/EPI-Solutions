from typing import Set

from test_framework import generic_test

from collections import deque
def transform_string(D: Set[str], s: str, t: str) -> int:
    queue = deque([(s, 0)])
    D.discard(s)

    def lower_case_chars():
        for i in range(ord('a'), ord('z')+1):
            yield chr(i)

    while queue:
        cur_str, transformations = queue.popleft()

        if cur_str == t:
            return transformations
        for i in range(len(cur_str)):
            for c in lower_case_chars():
                candidate = cur_str[:i] + c + cur_str[i+1:]
                if candidate in D:
                    D.discard(candidate)
                    queue.append((candidate, transformations+1))
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
