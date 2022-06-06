from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum
        return nums


s = Solution()
print(s.runningSum([1,2,3,4]))