from typing import List

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ""

class SolutionSplitSpace (Solution):
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(' ')
        lastIdx = min(k, len(words))
        return " ".join(words[:lastIdx])

class SolutionPointer (Solution):
    def truncateSentence(self, s: str, k: int) -> str:
        count = 0
        word = ''

        for c in s:
            if c == ' ':
                count += 1
            if count == k:
                break
            word += c
        return word


s: Solution = SolutionPointer()
print(s.truncateSentence("Hello how are you Contestant", 4))
print(s.truncateSentence("What is the solution to this problem", 4))
print(s.truncateSentence("chopper is not a tanuki", 5))
