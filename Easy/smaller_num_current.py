from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return []

class SolutionLoop (Solution):
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                if i != j and nums[i] > nums[j]:
                    ans[i] += 1
        return ans

class SolutionSortMap (Solution):
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = {}
        n = len(nums)
        ans = [0 for i in range(n)]
        sortedNums = sorted(nums)
        currentMax = sortedNums[0]

        for idx, num in enumerate(sortedNums):
            if num > currentMax:
                currentMax = num
                counts[num] = idx
        for idx, num in enumerate(nums):
            ans[idx] = counts[num] if num in counts else 0
        
        return ans

class SolutionSortSimple (Solution):
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(n)]
        sortedNums = sorted(nums)

        for idx, num in enumerate(nums):
            ans[idx] = sortedNums.index(num)
        return ans


s = SolutionSortMap()
print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(s.smallerNumbersThanCurrent([1, 1, 1, 1, 1]))