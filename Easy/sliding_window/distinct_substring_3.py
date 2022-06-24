from collections import deque

# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# 1876. Substrings of Size Three with Distinct Characters

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return 0

class SolutionSlidingWindowQueue (Solution):
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        k = 3
        start = 0
        end = 0
        queue = deque()

        while end < len(s):
            char = s[end]
            queue.append(char)

            # Slide window to the right
            if end - start + 1 < k:
                end += 1
            # If it matches K size
            else:
                unique = set(queue)
                # Check for unique values
                if len(unique) == k:
                    ans += 1

                queue.popleft()
                start +=1
                end += 1

        return ans


s: Solution = SolutionSlidingWindowQueue()
print(s.countGoodSubstrings("xyzzaz"))
print(s.countGoodSubstrings("aababcabc"))
print(s.countGoodSubstrings("icolgrjedehnd"))
