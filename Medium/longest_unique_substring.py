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

class SolutionSlidingWindow (Solution):
     def lengthOfLongestSubstring(self, s: str) -> int:
        ascii_chars = [0] * 128
        left = right = 0
        longest = 0

        # Expand the window to the right
        while right < len(s):
            # Store the character in the Set
            ascii_chars[ord(s[right])] += 1
            # If a duplicate character is found, collapse the window 
            # and remove all found letters until the Set is cleared
            while ascii_chars[ord(s[right])] > 1:
                ascii_chars[ord(s[left])] -= 1
                left += 1

            right += 1
            longest = max(longest, right - left)
            
        return longest


class SolutionOptimalSlidingWindow (Solution):
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_position = {}
        left = right = 0
        longest = 0

        for right in range(len(s)):
            ascii = ord(s[right])

            # If the character was already found, find the next index
            # of that character to change the window bounds
            if ascii in char_position:
                left = max(char_position[ascii], left)

            char_position[ascii] = right + 1
            longest = max(longest, right - left + 1)

        return longest
            

s: Solution = SolutionNaive()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("a"))

s: Solution = SolutionSlidingWindow()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("a"))

s: Solution = SolutionOptimalSlidingWindow()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("a"))
