from collections import defaultdict
import enum
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        return 0

class SolutionLoops (Solution):
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count

class SolutionLookup (Solution):
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0

        d = defaultdict(list)
        for idx, val in enumerate(nums):
            d[val].append(idx)
        
        for vals in d.values():
            # Any number with an identical pair will have more than one value in the list
            if len(vals) > 1:
                # Check if each index can be paired with 0
                for i in range(0, len(vals)):
                    for j in range(i + 1, len(vals)):
                        if (vals[i] * vals[j]) % k == 0:
                            count += 1
        return count


s: Solution = SolutionLookup()
print(s.countPairs([3, 1, 2, 2, 2, 1, 3], 2))
print(s.countPairs([1, 2, 3, 4], 1))
