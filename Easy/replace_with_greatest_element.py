from typing import List

# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/discuss/976461/Python-solution
# 1299. Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        return []

# REVIEW: Math - Greatest Number
# INTERVIEW: Candidate
class SolutionBrute (Solution):
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = list(arr)
        n = len(arr)

        for i in range(0, n):
            maxVal = 0
            for j in range(i + 1, n):
                maxVal = max(arr[j], maxVal)
            ans[i] = maxVal
        ans[n - 1] = -1
        return ans


class SolutionIterative (Solution):
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxVal = -1
        ans = [int] * n

        for i in range(n, 0, -1):
            curr = arr[i - 1]
            ans[i - 1] = maxVal
            maxVal = max(maxVal, curr)
        return ans


s: Solution = SolutionIterative()
print(s.replaceElements([17,18,5,4,6,1]))
print(s.replaceElements([400]))
