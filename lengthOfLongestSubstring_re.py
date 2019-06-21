'''
Quest:
    Given a string, find the length of the longest substring without repeating characters.

    Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
    "pwke" is a subsequence and not a substring.

Solution:
    - need pointers to indicate start point of sub.
    - need hash table to store the chr and its index, their count == 1

    for example, seq like "abc d efgh d ijklmn", start = 0, all the way to second "d", res = 8
    then start = 3+1, and all the way to "n", res = max(8, 11) = 11
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        hashTable = {}
        res = 0

        for i in range(len(s)):
            if hashTable.get(s[i], -1) != -1 and start <= hashTable[s[i]]:
                start = hashTable[s[i]] + 1
            else:
                res = max(res, i + 1 - start)

            hashTable[s[i]] = i

        return res

test = Solution()
x = "abcdefghdijklmn"
print(test.lengthOfLongestSubstring(x))