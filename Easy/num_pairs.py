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

"""
    REVIEW: Math - Total number of unique pairs in a list is N * (N - 1) / 2
    Explaination:
    
    List = ABCD
    Size (N) = 4

    Unique Pairs:
        AB
        AC
        AD
        BC
        BD
        CD

    Count of A pairs = 3 (N - 1)
    Count of B pairs = 2 (N - 2)
    Count of C pairs = 1 (N - 3)

    Total pairs count = 
        (N - 1) + (N - 2) + ... (N - (N - 1))   which simplifies to
        1 + 2 + ... N - 1                       which simplifies to
        N * (N - 1) / 2
"""
# https://stackoverflow.com/questions/18859430/how-do-i-get-the-total-number-of-unique-pairs-of-a-set-in-the-database#answer-37847498
class SolutionLoopLookupCount (Solution):
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            # Get the count of each distinct number. Can be used to find the unique pairs.
            counts[num] = counts.get(num, 0) + 1
        # Permutation of pairs in a list of n size is n * n-1 / 2
        return int(sum(n * (n-1) * 0.5 for n in counts.values()))


s = SolutionLoopLookupIterative()
print(s.numIdenticalPairs([1,2,3,1,1,3]))
print(s.numIdenticalPairs([1,1,1,1]))
print(s.numIdenticalPairs([1,2,3]))