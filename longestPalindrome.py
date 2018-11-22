'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""

        for i in range(len(s)):
            tmp = self.palindrome(s, i, i)
            if len(tmp) > len(res):
                res = tmp

            tmp = self.palindrome(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp

        return res

    def palindrome(self, s, l, r): # return the max palindrome based on given parameter
        while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
        return s[(l+1):r]