from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return 0

class SolutionIterative (Solution):
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idxMap = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        count = sum(1 if ruleValue == item[idxMap[ruleKey]] else 0 for item in items)
        return count


s: Solution = SolutionIterative()
print(s.countMatches(
    [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
    'color',
    'silver'
))

print(s.countMatches(
    [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
    'type',
    'phone'
))