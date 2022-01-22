import enum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return []

class SolutionBruteForce (Solution):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

class SolutionLookup (Solution):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_lookup = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in diff_lookup:
                return [diff_lookup[diff], index]
            diff_lookup[num] = index
        
        return None

s: Solution = SolutionLookup()

print(s.twoSum([3,2,4], 6))
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,3], 6))
print(s.twoSum([3,2,2,2,3], 6))
