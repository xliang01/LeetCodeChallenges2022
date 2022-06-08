from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        return []

class SolutionIterative (Solution):
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [0] * (len(encoded) + 1)
        decoded[0] = first

        for idx in range(1, len(decoded)):
            decoded[idx] = encoded[idx - 1] ^ decoded[idx - 1]
        return decoded


s: Solution = SolutionIterative()
print(s.decode([1, 2, 3], 1))
print(s.decode([6, 2, 7, 3], 4))
print(s.decode([6], 1))
