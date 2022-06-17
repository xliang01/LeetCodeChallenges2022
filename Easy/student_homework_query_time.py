from typing import List

# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
# 1450. Number of Students Doing Homework at a Given Time

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return 0

class SolutionIterative (Solution):
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for i in range(0, len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                ans += 1
        return ans

s: Solution = SolutionIterative()
print(s.busyStudent([1, 2, 3], [3, 2, 7], 4))
print(s.busyStudent([4], [4], 4))
print(s.busyStudent([5, 6, 7], [10, 10, 10], 9))
