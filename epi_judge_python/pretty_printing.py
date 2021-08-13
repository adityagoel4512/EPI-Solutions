from typing import List

from test_framework import generic_test
from functools import lru_cache

def minimum_messiness(words: List[str], line_length: int) -> int:
    # let M(i, remaining_len) => minimum messiness for words[i:] with the final line having remaining_len length
    # M(len(words), remaining_len) = remaining_len
    # M(i, cur_len): if remaining_len < len(words[i])+1: remaining_len + M(i, line_length))
    # M(i, cur_len): if remaining_len >= len(words[i])+1: min(remaining_len + M(i, line_length), M(i+1, line_length-len(words[i])-1))
    @lru_cache(maxsize=None)
    def helper(i, remaining_len):
        if i == len(words):
            return remaining_len*remaining_len
        elif remaining_len < len(words[i])+1:
            return remaining_len*remaining_len + helper(i, line_length)
        elif remaining_len == line_length:
            return helper(i+1, remaining_len-len(words[i]))
        else:
            return min(remaining_len*remaining_len + helper(i, line_length), helper(i+1, remaining_len-len(words[i])-1))

    return helper(0, line_length)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
