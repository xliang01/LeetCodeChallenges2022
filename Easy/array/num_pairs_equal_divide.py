from collections import defaultdict
from typing import List, Set

# https://leetcode.com/problems/divide-array-into-equal-pairs/
# 2206. Divide Array Into Equal Pairs

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return False

class SolutionLookupCount (Solution):
    def divideArray(self, nums: List[int]) -> bool:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        for c in d.values():
            if c % 2 != 0:
                return False
        return True

class SolutionSet (Solution):
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return len(s) == 0


s: Solution = SolutionSet()
print(s.divideArray([3,2,3,2,2,2]))
print(s.divideArray([1,2,3,4]))