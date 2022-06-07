from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return 0

class SolutionStringMatch:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for op in operations:
            if op == "X++" or op == "++X":
                ans += 1
            else:
                ans -= 1
        return ans


class SolutionOneLiner:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if x == "X++" or x == "++X" else -1 for x in operations)

s: Solution = SolutionOneLiner()
print(s.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
