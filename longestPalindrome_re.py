'''
Quest:
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:
    Input: "cbbd"
    Output: "bb"

Solution:
    - stack?
        imaging given "abbacdefgfedc", first stack "a" and "b" in, we continue check s[i] == stack[-1] or s[i+1] == stack[-1]
        if s[i] == stack[-1]: stack.pop(), res += 1
        if s[i+1] == stack[-1]: i += 1, stack.pop(), res +=2

    - use recursion instead
        self.palindrome(s, start, end):
            return the longest palindromic substring, which the middle point is start and end
'''


class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            tmp1 = self.palindrome(s, i, i)
            tmp2 = self.palindrome(s, i, i+1)
            if len(tmp1) > len(res):
                if len(tmp2) > len(tmp1):
                    res = tmp2
                else:
                    res = tmp1
            else:
                if len(tmp2) > len(res):
                    res = tmp2

        return res


    def palindrome(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[(start+1):end]

test = Solution()
x = "abbacdefgfedc"
print(test.longestPalindrome(x))