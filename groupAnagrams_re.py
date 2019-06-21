'''
Quest:
    Given an array of strings, group anagrams together.

    Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

    Note:
    All inputs will be in lowercase.
    The order of your output does not matter.

Solution:
    - hash table, but not for each elements, for the whole list instead
    - sorted anagram gonna look exactly the same
'''


class Solution(object):
    def groupAnagrams(self, strs):
        res = {}

        for s in strs:
            key = tuple(sorted(s))
            res[key] = res.get(key, []) + [s]

        return list(res.values())

test = Solution()
x = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(test.groupAnagrams(x))