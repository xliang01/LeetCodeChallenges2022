from typing import List

# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# 1304. Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return []

class SolutionSymmetry (Solution):
    def sumZero(self, n: int) -> List[int]:
        mid = n // 2
        ans = [int] * n

        for i in range(0, mid):
            ans[i] = i + 1
            ans[n - 1 - i] = -ans[i]
        if n % 2 != 0:
            ans[mid] = 0

        return ans

s: Solution = SolutionSymmetry()
print(s.sumZero(3))
print(s.sumZero(1))
