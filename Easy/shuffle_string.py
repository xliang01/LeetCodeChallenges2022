from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return 0

class SolutionIterativeReplace (Solution):
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [str] * len(indices)
        for idx, c in enumerate(s):
            offsetIdx = indices[idx]
            ans[offsetIdx] = c
        return "".join(ans)


s: Solution = SolutionIterativeReplace()
print(s.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
print(s.restoreString("abc", [0, 1, 2]))
