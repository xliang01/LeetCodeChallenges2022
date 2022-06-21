from typing import List

# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# 1475. Final Prices With a Special Discount in a Shop

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        return []

class SolutionLoop (Solution):
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n

        for i in range(0, n):
            ans[i] = prices[i]
            for j in range(i + 1, n):
                if prices[i] >= prices[j]:
                    ans[i] = prices[i] - prices[j]
                    break
        return ans

# REVIEW: DS - Stack
class SolutionStack(Solution):
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        # We can keep a stack of the index in the original array.
        # If we iterate through prices and determine if the stack
        # contains a previous number (via the index) that's greater,
        # then update the previous value at the stored index in the 
        # stack. This "back" updates the array, while utilizing the 
        # stack.
        # 
        # Runtime is O(N) because we at most push and pop each number
        # just once, so we have 2N operations, which is O(N).  
        stack = []
        
        for idx, v in enumerate(prices):
            ans[idx] = v
            while stack and prices[stack[-1]] >= v:
                prevIdx = stack.pop()
                ans[prevIdx] = prices[prevIdx] - v
            stack.append(idx)
        return ans


s: Solution = SolutionStack()
print(s.finalPrices([8,4,6,2,3]))
print(s.finalPrices([1,2,3,4,5]))
print(s.finalPrices([10,1,1,6]))