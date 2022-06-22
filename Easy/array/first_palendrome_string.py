from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return ""

class SolutionIterative (Solution):
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self._isPalindrome_(word):
                return word
        return ""
    
    def _isPalindrome_(self, word: str) -> bool:
        n = len(word)
        for i in range(0, int(n / 2)):
            if word[i] != word[n - 1 - i]:
                return False
        return True

class SolutionSimple (Solution):
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


s: Solution = SolutionSimple()
print(s.firstPalindrome(["abc","car","ada","racecar","cool"]))
print(s.firstPalindrome(["notapalindrome","racecar"]))
print(s.firstPalindrome(["def","ghi"]))