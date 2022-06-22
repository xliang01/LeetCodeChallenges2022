from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return []

class SolutionNewArrayInsert:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [int] * 2 * n
        ansIdx = 0
        for i in range(0, n):
            ans[ansIdx] = nums[i]
            ans[ansIdx + 1] = nums[n + i]
            ansIdx += 2
        return ans


s: Solution = SolutionNewArrayInsert()
print(s.shuffle([2,5,1,3,4,7], 3))
