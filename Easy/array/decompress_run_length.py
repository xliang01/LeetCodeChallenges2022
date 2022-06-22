from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return []

class SolutionIterative (Solution):
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        total = sum(nums[idx] for idx in range(0, len(nums), 2))
        ans = [int] * total
        ansIdx = 0

        for idx in range(0, len(nums), 2):
            freq = nums[idx]
            val = nums[idx + 1]
            for i in range(0, freq):
                ans[ansIdx] = val
                ansIdx += 1
        return ans


s: Solution = SolutionIterative()
print(s.decompressRLElist([1,2,3,4]))
print(s.decompressRLElist([5, 1]))