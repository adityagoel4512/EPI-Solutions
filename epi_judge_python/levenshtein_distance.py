from test_framework import generic_test
from functools import lru_cache

def levenshtein_distance(A: str, B: str) -> int:
    # helper(i, j) denotes the distance between A[:i] and B[:j]
    @lru_cache(None)
    def helper(i, j):
        if i == len(A):
            return len(B)-j
        elif j == len(B):
            return len(A)-i

        edits = (A[i] != B[j]) + helper(i+1, j+1)
        deletes = 1 + helper(i+1, j)
        additions = 1 + helper(i, j+1)
        return min(edits, deletes, additions)

    return helper(0, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
