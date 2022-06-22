from collections import defaultdict
from re import S
from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        return 0

class SolutionLookup (Solution):
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        d = {}
        d = defaultdict(lambda: 0, d)
        maxSize = 0

        for r in rectangles:
            side = min(r[0], r[1])
            maxSize = max(maxSize, side)
            d[side] += 1
        
        return d[maxSize]


s: Solution = SolutionLookup()
print(s.countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
print(s.countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]]))
