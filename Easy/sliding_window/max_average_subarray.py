from typing import List

# https://leetcode.com/problems/maximum-average-subarray-i/submissions/
# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return 0.0

class SolutionIterative (Solution):
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running_total = sum(nums[0: k])
        ans = running_total
        offset = k - 1

        for i in range(1, len(nums) - offset):
            running_total = running_total + nums[i + offset] - nums[i - 1]
            ans = max(ans, running_total)
        return ans / k

s: Solution = SolutionIterative()
# print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
# print(s.findMaxAverage([5], 1))
# print(s.findMaxAverage([-1], 1))
# print(s.findMaxAverage([0, 1, 1, 3, 3], 4))
# print(s.findMaxAverage([0, 4, 0, 3, 2], 1))
print(s.findMaxAverage([4, 2, 1, 3, 3], 2))
