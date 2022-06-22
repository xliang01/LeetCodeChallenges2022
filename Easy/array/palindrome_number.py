from reprlib import recursive_repr


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False


class SolutionString (Solution):
    def isPalindrome(self, x: int) -> bool:
        s = f'{x}'
        n = len(s)

        if n == 1:
            return True

        for i in range(int(n / 2)):
            if s[i] != s[n-1-i]:
                return False
        return True


class SolutionReverseNumber(Solution):
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers automatically not a palindrome
        if x < 0:
            return False
        # Single digit numbers are automatically a palindrome
        elif x < 10:
            return True
        # Any multiples of 10 is not a palindrome because the first digit is never 0
        elif (x % 10 == 0) and x != 0:
            return False

        reversed = 0
        # Reverse the number until the half way point
        while x > reversed:
            last_digit = x % 10
            # Get the last digit and add to the previous value, incremented by base 10. This reverses the value.
            reversed = last_digit + (reversed * 10)
            # Remove the last digit so the next digit can be reversed
            x = int(x / 10)

        # Either the reversed value matches exactly with an even digit number, or we get rid of the last
        # number for an odd digit number. For odd digit numbers, the last digit is the center number that
        # does not matter because it's the anchor in a palindrome.
        return x == reversed or x == int(reversed / 10)


# s: Solution = SolutionString()
# print(s.isPalindrome(-1))
# print(s.isPalindrome(1))
# print(s.isPalindrome(22))
# print(s.isPalindrome(23))
# print(s.isPalindrome(121))
# print(s.isPalindrome(123123))
# print(s.isPalindrome(1000021))

print("---")

s: Solution = SolutionReverseNumber()
# print(s.isPalindrome(-1))
# print(s.isPalindrome(1))
# print(s.isPalindrome(22))
# print(s.isPalindrome(23))
print(s.isPalindrome(10))
# print(s.isPalindrome(121))
# print(s.isPalindrome(123123))
# print(s.isPalindrome(1300021))
