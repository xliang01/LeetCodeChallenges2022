from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return 0

class SolutionRecursiveBackTrack (Solution):
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        return self._combo_(nums, subset, 0)

    def _subset_(self, nums: List[int], subset: List[int], idx: int) -> int:
        v = 0
        for s in subset:
            v ^= s

        for j in range(idx, len(nums)):
            subset.append(nums[j])
            v += self._combo_(nums, subset, j + 1)
            subset.pop(-1)

        return v

# REVIEW: Algo - Backtracking
class SolutionBackTrackSimple (Solution):
    # Finding all subsets can be found https://www.youtube.com/watch?v=SHsGi38sHSQ&t=465s
    # It requires a recusive algorithm with including the possibility, and excluding the
    # possibility. Therefore we want to add all the possiblities together.
    #
    # Note: Total run time is O(2^n) since we need to traverse all possibilities of either
    # include or exclude.
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(nums: List[int], index: int, xorVal: int):
            if index == len(nums):
                return xorVal
            # Include the xor of the current element
            include = dfs(nums, index + 1, xorVal ^ nums[index])
            # Exclude the xor of the current element
            exclude = dfs(nums, index + 1, xorVal)
            # Get the sum
            return include + exclude

        return dfs(nums, 0, 0)


s: Solution = SolutionBackTrackSimple()
print(s.subsetXORSum([5, 1, 6]))
print(s.subsetXORSum([3, 4, 5, 6, 7, 8]))
