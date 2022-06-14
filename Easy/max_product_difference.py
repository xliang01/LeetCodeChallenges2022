from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return 0

class SolutionSort (Solution):
    def maxProductDifference(self, nums: List[int]) -> int:
        sortNums = sorted(nums)
        minPair = sortNums[0] * sortNums[1]
        maxPair = sortNums[-1] * sortNums[-2]
        return maxPair - minPair

class SolutionIterativeMinMax (Solution):
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = 100001

        for n in nums:
            if n >= max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n

            if n <= min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        return (max1 * max2) - (min1 * min2)


s: Solution = SolutionIterativeMinMax()
print(s.maxProductDifference([5, 6, 2, 7, 4]))
print(s.maxProductDifference([4,2,5,9,7,4,8]))
print(s.maxProductDifference([1,6,7,5,2,4,10,6,4]))