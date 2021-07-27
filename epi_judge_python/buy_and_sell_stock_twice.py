from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    first_transaction_max_profits = [0.0] * len(prices)
    min_price_so_far = float('inf')
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        first_transaction_max_profits[i] = max(0.0 if i == 0 else first_transaction_max_profits[i-1], price - min_price_so_far)
    
    # first_transaction_max_profits[i] is the max profit obtained by buying before day i and selling on day i (0..N-1)
    # find max profit from day i+1 onwards
    max_price_so_far = float('-inf')
    max_total_profit = max(0.0, max(first_transaction_max_profits))
    for i, price in reversed(list(enumerate(prices))):
        if i != 0:
            max_price_so_far = max(max_price_so_far, price)
            max_total_profit = max(max_total_profit, max_price_so_far-price+first_transaction_max_profits[i-1])
 
    return max_total_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
