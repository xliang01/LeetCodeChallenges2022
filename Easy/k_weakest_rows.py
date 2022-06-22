from typing import List
import heapq

# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# 1337. The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return []

class SolutionPriorityQueue (Solution):
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, r in enumerate(mat):
            total = sum(r)
            heapq.heappush(heap, (total, i))
        
        ans = []
        for i in range(0, k):
            ans.append(heapq.heappop(heap)[1])
        return ans


s: Solution = SolutionPriorityQueue()
print(s.kWeakestRows([[1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1]], 3))

print(s.kWeakestRows([[1, 0, 0, 0],
                      [1, 1, 1, 1],
                      [1, 0, 0, 0],
                      [1, 0, 0, 0]], 2))