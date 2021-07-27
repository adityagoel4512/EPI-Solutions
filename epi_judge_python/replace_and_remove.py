import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    def remove_char(c):
        w = 0
        final_len = 0
        for i in range(size):
            if s[i] != c:
                s[w] = s[i]
                w += 1
                final_len += 1 if s[i] != 'a' else 2
        return w, final_len
            
    w, new_len = remove_char('b')
    def insert_char(prev):
        r = prev-1
        w = new_len-1
        for i in range(r, -1, -1):
            if s[i] == 'a':
                s[w] = 'd'
                s[w-1] = 'd'
                w -= 2
            else:
                s[w] = s[i]
                w -= 1
        
    insert_char(w)        
    return new_len
@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
