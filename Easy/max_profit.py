from typing import List
from xmlrpc.client import MAXINT, MININT

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return 0

class SolutionNaive (Solution):
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                profit = max(profit, prices[j] - prices[i])
        return profit

class SolutionSliding (Solution):
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
        

s: Solution = SolutionNaive()
print(s.maxProfit([1]))
print(s.maxProfit([1, 2, 3, 2, 3, 4]))
print(s.maxProfit([3, 2, 1, 4, 3, 2, 5]))
print(s.maxProfit([3, 6, 9, 1, 2, 3]))
print(s.maxProfit([8, 10, 1, 7]))

print(s.maxProfit([3, 6, 4, 10]))
print(s.maxProfit([2, 6, 1, 10]))
print(s.maxProfit([4, 3, 2, 1]))
