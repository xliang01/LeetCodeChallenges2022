from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        return 0

class SolutionSort (Solution):
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        ans = 100001

        for i in range(0, len(sorted_nums)-k+1):
            max_val = sorted_nums[i + k - 1]
            min_val = sorted_nums[i]
            ans = min(ans, max_val - min_val)
        return ans

s: Solution = SolutionSort()
print(s.minimumDifference([90], 1))
print(s.minimumDifference([9, 4, 1, 7], 2))

