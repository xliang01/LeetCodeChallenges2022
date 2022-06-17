from typing import List

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# 1295. Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return 0

class SolutionDivideBy10 (Solution):
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            d = 1
            while n // 10 > 0:
                d += 1
                n //= 10
            ans += 1 if d % 2 == 0 else 0
        return ans


s: Solution = SolutionDivideBy10()
print(s.findNumbers([12, 345, 2, 6, 7896]))
print(s.findNumbers([555, 901, 482, 1771]))
