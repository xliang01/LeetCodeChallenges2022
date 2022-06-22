from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return 0

# REVIEW: Math - Min between two points
class SolutionMax (Solution):
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        if n == 1:
            return ans
        
        for i in range(0, len(points) - 1):
            currentP = points[i]
            nextP = points[i + 1]
            ans += max(abs(nextP[0] - currentP[0]), abs(nextP[1] - currentP[1]))
        
        return ans


s: Solution = SolutionMax()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))