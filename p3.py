"""
You are given an array of historical stock prices per day
[6, 13, 2, 10, 3, 5]
write an algorithm that figures out what days(index of array)
you could buy and sell the stock for maximum profit
"""
from typing import List


def stock_profit(arr: List):
    min_price = arr[0]
    max_profit = 0
    for price in arr:
        min_price = min(price, min_price)
        current_profit = price - min_price
        max_profit = max(current_profit, max_profit)
    return max_profit


print(stock_profit([6, 13, 2, 10, 3, 5]))
