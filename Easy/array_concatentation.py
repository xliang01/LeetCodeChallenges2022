from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return []

class SolutionLinear (Solution):
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [int] * n * 2

        for i in range(0, n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans

s: Solution = SolutionLinear()
print(s.getConcatenation([0, 1, 2]))