from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return 0

class SolutionStringSplit (Solution):
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = 0
        for s in sentences:
            most = max(most, len(s.split(" ")))
        return most

class SolutionStringSplitSimple (Solution):
    def mostWordsFound(self, sentences: List[str]) -> int:
       return max(len(s.split(" ")) for s in sentences)


class SolutionSpaceCountSimple (Solution):
    def mostWordsFound(self, sentences: List[str]) -> int:
       return max(s.count(" ") + 1 for s in sentences)


s: Solution = SolutionStringSplitSimple()
print(s.mostWordsFound(["please wait a minute", "continue to fight", "continue to win"]))
