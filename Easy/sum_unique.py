from collections import defaultdict
from typing import List

# https://leetcode.com/problems/sum-of-unique-elements/submissions/
# 1748. Sum of Unique Elements

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return 0

class SolutionMapCount (Solution):
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        counts = defaultdict(int)

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for n, v in counts.items():
            if v == 1:
                ans += n
        return ans

class SolutionMapBool (Solution):
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        bools = defaultdict(bool)

        for n in nums:
            if n not in bools:
                bools[n] = False
                ans += n
            elif n in bools and bools[n] == False:
                ans -= n
                bools[n] = True
        return ans

class SolutionNumberBucket (Solution):
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        bucket = [0] * 101

        for n in nums:
            bucket[n] += 1

        for idx, val in enumerate(bucket):
            if val == 1:
                ans += idx

        return ans


s: Solution = SolutionNumberBucket()
print(s.sumOfUnique([1,2,3,2]))
print(s.sumOfUnique([1,1,1,1,1]))
print(s.sumOfUnique([1,2,3,4,5]))