'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map  ={} # storing the latest index of char '.'

        start = max_len = 0
        for i in range(len(s)):
            if hash_map.has_key(s[i]) and start <= hash_map[s[i]]: # start <= hash_map[s[i]] is in case of conditions like 'tmmsdfgt'
                start = hash_map[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)

            hash_map[s[i]] = i

        return max_len