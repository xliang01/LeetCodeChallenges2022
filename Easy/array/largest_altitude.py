from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return 0

class SolutionIterative (Solution):
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        total = 0
        for g in gain:
            total += g
            ans = max(ans, total)
        return ans


s: Solution = SolutionIterative()
print(s.largestAltitude([-5, 1, 5, 0, -7]))
print(s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
