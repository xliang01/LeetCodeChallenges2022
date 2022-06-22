from typing import List

# https://leetcode.com/problems/counting-words-with-a-given-prefix/
# 2185. Counting Words With a Given Prefix

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return 0

class SolutionIterative (Solution):
    def prefixCount(self, words: List[str], pref: str) -> int:
        pl = len(pref)
        ans = 0

        for word in words:
            if len(word) < pl:
                continue
            elif word[0:pl] == pref:
                ans += 1
        return ans

s: Solution = SolutionIterative()
print(s.prefixCount(["pay", "attention", "practice", "attend"], "at"))
print(s.prefixCount(["leetcode", "win", "loops", "success"], "code"))

