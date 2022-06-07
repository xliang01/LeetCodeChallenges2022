from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return 0

class SolutionLoopBruteForce (Solution):
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    pairs += 1
        return pairs

class SolutionLoopLookupIterative (Solution):
    def numIdenticalPairs(self, nums: List[int]) -> int:
        idxMap = {}
        pairs = 0
        for idx, num in enumerate(nums):
            if num not in idxMap:
                idxMap[num] = [idx]
            else:
                pairs += len(idxMap[num])
                idxMap[num].append(idx)
        return pairs

class SolutionLoopLookupCount (Solution):
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
           counts[num] = counts.get(num, 0) + 1
        # Permutation of pairs in a list of n size is n * n-1 / 2
        return int(sum(n * (n-1) * 0.5 for n in counts.values()))


s = SolutionLoopLookupIterative()
print(s.numIdenticalPairs([1,2,3,1,1,3]))
print(s.numIdenticalPairs([1,1,1,1]))
print(s.numIdenticalPairs([1,2,3]))