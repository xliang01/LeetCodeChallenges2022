class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return 0

class SolutionNaive (Solution):
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if self.checkUnique(i, j, s):
                    longest = max(longest, j - i + 1)

        return longest

    def checkUnique(self, start: int, end: int, s: str) -> bool:
        # Initiates an integer array with 128 length
        ascii_chars = [0] * 128
        for k in range(start, end + 1):
            # ord transforms a character to the ascii value
            ascii = ord(s[k])
            ascii_chars[ascii] += 1
            if ascii_chars[ascii] > 1:
                return False
        return True

s: Solution = SolutionNaive()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("a"))
