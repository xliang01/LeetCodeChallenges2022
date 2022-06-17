from audioop import reverse
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return 0

class SolutionModIterative (Solution):
    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)

        for i in range(minNum, 1, -1):
            if maxNum % i == 0 and minNum % i == 0:
                return i
        return 1


# REVIEW: Math - Euclidean
class SolutionEuclidean (Solution):
    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)

        # Using Euclidean Equation, we can find the common
        # denominator between two numbers based with MOD and
        # remainders.
        while minNum != 0:
            # Use remainder to determine if it's divisible
            temp = minNum
            # Find new remainder from max and min
            minNum = maxNum % minNum
            # Declare max from previous min
            maxNum = temp
        return maxNum

s: Solution = SolutionEuclidean()
print(s.findGCD([2,5,6,9,10]))
print(s.findGCD([7,5,6,8,3]))
print(s.findGCD([3,3]))
print(s.findGCD([6,9]))
print(s.findGCD([12,20]))