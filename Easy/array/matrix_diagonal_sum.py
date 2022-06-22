from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return 0


class SolutionIterative (Solution):
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]

        ans = 0
        center = int(n / 2)
        i = 0
        
        while i < int(n / 2):
            j = n - 1 - i
            # Add top matrix
            ans += mat[i][i] + mat[i][j]
            # Add bottom matrix
            ans += mat[j][i] + mat[j][j]
            i += 1

        # If odd matrix, add center
        if n % 2 != 0:
            ans += mat[center][center]

        return ans

s: Solution = SolutionIterative()
print(s.diagonalSum([[1]]))

print(s.diagonalSum([[1, 2],
                     [3, 4]]))

print(s.diagonalSum([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]))

print(s.diagonalSum([[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]]))
