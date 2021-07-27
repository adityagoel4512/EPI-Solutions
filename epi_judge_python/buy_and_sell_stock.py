from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price = None
    max_profit = 0.0
    for price in prices:
        if min_price is not None:
            max_profit = max(max_profit, price-min_price) 
        if min_price is None:
            min_price = price
        else:
            min_price = min(min_price, price)
        
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
