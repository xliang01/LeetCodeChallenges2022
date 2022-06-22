from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 0

class SolutionIterativeDiff (Solution):
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        ans = 0
        prevMax = nums[0]
        for idx in range(1, n):
            current = nums[idx]
            if current > prevMax:
                prevMax = current
            else:
                ops = (prevMax - current) + 1
                prevMax = current + ops
                ans += ops
        return ans


s: Solution = SolutionIterativeDiff()
print(s.minOperations([1, 1, 1]))
print(s.minOperations([1,5,2,4,1]))