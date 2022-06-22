from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        return []

class SolutionInsert (Solution):
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for idx, offsetIdx in enumerate(index):
            num = nums[idx]
            ans.insert(offsetIdx, num)
        return ans


s: Solution = SolutionInsert()
print(s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
print(s.createTargetArray([1], [0]))