from typing import List

from test_framework import generic_test
from functools import lru_cache

def maximum_revenue(coins: List[int]) -> int:
    @lru_cache(maxsize=None)
    def revenue(i, j):
        if i > j:
            return 0
        else:
            return max(coins[i] + min(revenue(i+1, j-1), revenue(i+2, j)), coins[j] + min(revenue(i+1, j-1), revenue(i, j-2)))

    # R(i, j) = max(coins[i] + min(R(i+1, j-1), R(i+2, j)), coins[j] + min(R(i+1, j-1), R(i, j-2)))
    # R(i, j) : i > j => 0
    return revenue(0, len(coins)-1)
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
