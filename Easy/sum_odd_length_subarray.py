from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return 0

class SolutionBruteForce (Solution):
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        size = 1
        ans = 0

        while size <= n:
            start = 0
            while True:
                end = start + size - 1
                if end >= n:
                    break
                ans += sum(arr[i] for i in range(start, end + 1))
                start += 1
            size += 2
        return ans

# https://www.youtube.com/watch?v=J5IIH35EBVE
class SolutionMathCount (Solution):
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for idx, val in enumerate(arr):
            # NOTE: Total combination for a number starting and ending at index i is (n - index) * (index + 1)
            # This is similar to finding the total number of paths from point A to point C through some B.
            totalCount = (n - idx) * (idx + 1)
            oddCount = int(totalCount / 2)
            # Odd total counts means the odd number of sub arrays is n / 2 + 1
            if totalCount % 2 == 1:
                oddCount += 1
            ans += (oddCount * val)

        return ans


s: Solution = SolutionMathCount()
print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
print(s.sumOddLengthSubarrays([1, 2]))
print(s.sumOddLengthSubarrays([10,11,12]))