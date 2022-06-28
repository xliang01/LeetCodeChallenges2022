from typing import List

# https://leetcode.com/problems/find-the-k-beauty-of-a-number/
# 2269. Find the K-Beauty of a Number

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        return 0

class SolutionSlidingWindow (Solution):
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        ans = 0

        for i in range(0, n-k+1):
            sub_value = int(s[i: i + k])
            if sub_value != 0 and num % sub_value == 0:
                ans += 1
        return ans

s: Solution = SolutionSlidingWindow()
print(s.divisorSubstrings(240, 2))
print(s.divisorSubstrings(430043, 2))
print(s.divisorSubstrings(2, 1))
