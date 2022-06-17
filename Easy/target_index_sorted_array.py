from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return []

class SolutionSimple (Solution):
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        return [idx for idx, val in enumerate(sortedNums) if val == target]

# REVIEW: Math - Array Index Position Using Counting
class SolutionIterativeCount (Solution):
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = 0
        same = 0

        # Find the frequency of numbers less than the target. Since the list 
        # is eventually sorted, only numbers less than the target will appear in
        # ascending order. Therefore, the count of smaller numbers will be used
        # as the starting index for target. Then just count how manu numbers match
        # the target, and use that as the end index.
        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                same += 1
        return [idx for idx in range(smaller, smaller + same)]


s: Solution = SolutionIterativeCount()
print(s.targetIndices([1,2,5,2,3], 2))
print(s.targetIndices([1,2,5,2,3], 3))
print(s.targetIndices([1,2,5,2,3], 5))