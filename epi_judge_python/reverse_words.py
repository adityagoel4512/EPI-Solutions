import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
from collections import deque
def reverse_words(s):
    result = []
    tmp = deque()
    for c in reversed(s):
        if c == ' ':
            result.extend(tmp)
            result.append(' ')
            tmp = deque()
        else:
            tmp.appendleft(c)
    result.extend(tmp)
    for i in range(len(s)):
        s[i] = result[i]
    
@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
