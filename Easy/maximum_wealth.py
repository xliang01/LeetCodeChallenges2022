from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return 0

class SolutionIterative (Solution):
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_amount = 0
        for account in accounts:
            max_amount = max(max_amount, self.accountTotal(account))
        return max_amount

    def accountTotal(self, account: List[int]) -> int:
        sum = 0
        for item in account:
            sum += item
        return sum

class SolutionIterativeSimple (Solution):
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)


s = SolutionIterativeSimple()
print(s.maximumWealth([[1,2,3],[3,2,1]]))