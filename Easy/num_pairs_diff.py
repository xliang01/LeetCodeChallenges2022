from collections import defaultdict
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return 0

class SolutionLoop (Solution):
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans

# REVIEW: Algo - Hashmap Counting
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/2064524/Python-1-Line-O(N2)-and-Short-O(N)
class SolutionMap (Solution):
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        counts = defaultdict(int)
        for num in nums:
            ans += counts[num + k] + counts[num - k]
            counts[num] += 1
        return ans


s: Solution = SolutionMap()
print(s.countKDifference([1, 2, 2, 1], 1))
print(s.countKDifference([1,3], 3))
print(s.countKDifference([3,2,1,5,4], 2))