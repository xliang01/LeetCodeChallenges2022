from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return []

class SolutionLambda (Solution):
    def buildArray(self, nums: List[int]) -> List[int]:
        return list(map(lambda i: nums[i], nums))

class SolutionArrayIndex (Solution):
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        for index in nums:
            ans[index] = nums[nums[index]]
        return ans

class SolutionOneLine (Solution):
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]


s: Solution = SolutionOneLine()
print(s.buildArray([0, 2, 1, 5, 3, 4]))
