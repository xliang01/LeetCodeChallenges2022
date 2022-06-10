from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return False

class SolutionPointers (Solution):
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        cIdx1 = cIdx2 = wIdx1 = wIdx2 = 0

        while wIdx1 < len(word1) and wIdx2 < len(word2):
            if word1[wIdx1][cIdx1] != word2[wIdx2][cIdx2]:
                return False

            if cIdx1 == len(word1[wIdx1]) - 1:
                cIdx1 = 0
                wIdx1 += 1
            else:
                cIdx1 += 1
    
            if cIdx2 == len(word2[wIdx2]) - 1:
                cIdx2 = 0
                wIdx2 += 1
            else:
                cIdx2 += 1

        return (
            # Must scan through all characters at the end of the word (should be 0)
            cIdx1 == cIdx2 and
            # Must scan through all words so it's at the end
            wIdx1 == len(word1) and wIdx2 == len(word2)
        )

s: Solution = SolutionPointers()
print(s.arrayStringsAreEqual(["ab" "c"], ["a", "bc"]))
print(s.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
print(s.arrayStringsAreEqual(["a" "c"], ["a", "b"]))
print(s.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefgh"]))
print(s.arrayStringsAreEqual(["a"], ["a", "b"]))
