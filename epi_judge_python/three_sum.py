from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    def has_two_sum(v):
        target = t-v
        i = 0
        j = len(A)-1
        while i <= j:
            total = A[i] + A[j]
            if total == target:
                return True
            elif total < target:
                i += 1
            else: # total > target
                j -= 1
        return False

    return any(has_two_sum(v) for v in A)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
