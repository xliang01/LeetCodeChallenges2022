from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return []

class SolutionMaxIterative (Solution):
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans = [bool] * len(candies)
        for idx, c in enumerate(candies):
            ans[idx] = c + extraCandies >= maxCandies
        return ans


s: Solution = SolutionMaxIterative()
print(s.kidsWithCandies([2, 3, 5, 1, 3], 3))
print(s.kidsWithCandies([4, 2, 1, 1, 2], 1))


