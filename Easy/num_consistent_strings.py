from typing import List
from xmlrpc.client import Boolean

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return 0

class SolutionLookupChar:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def toAscii(val: str) -> int:
            return ord(val) - ord('a')

        ascii = [False] * 26
        ans = 0
        
        for char in allowed:
            ascii[toAscii(char)] = True

        for word in words:
            match = True
            for char in word:
                if not ascii[toAscii(char)]:
                    match = False
                    break
            if match:
                ans += 1
        return ans


class SolutionSet (Solution):
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowedSet = set(allowed)

        for word in words:
            match = True
            for char in word:
                if not char in allowedSet:
                    break
            else:
                ans += 1
        return ans


s: Solution = SolutionSet()
print(s.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(s.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(s.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
