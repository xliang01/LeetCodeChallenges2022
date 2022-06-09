from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return 0

class SolutionSort (Solution):
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sortedSeats = sorted(seats)
        sortedStudents = sorted(students)
        return sum(abs(sortedSeats[i] - sortedStudents[i]) for i in range(0, len(seats)))

# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/discuss/1539518/O(n)-counting-sort-in-Python
class SolutionNumberBucket (Solution):
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seatsCount = [0] * (max(seats) + 1)
        studentsCount = [0] * (max(students) + 1)

        for v in seats:
            seatsCount[v] += 1
        for v in students:
            studentsCount[v] += 1
        
        ans = 0
        seatIdx = 1
        studentIdx = 1

        while seatIdx < len(seatsCount):
            if seatsCount[seatIdx]:
                while studentIdx < len(studentsCount) and not studentsCount[studentIdx]:
                    studentIdx += 1
                ans += abs(seatIdx - studentIdx)
                studentsCount[studentIdx] -= 1
                seatsCount[seatIdx] -= 1
            else:
                seatIdx += 1
        return ans


s: Solution = SolutionNumberBucket()
print(s.minMovesToSeat([3,1,5], [2,7,4]))
print(s.minMovesToSeat([4,1,5,9], [1,3,2,6]))