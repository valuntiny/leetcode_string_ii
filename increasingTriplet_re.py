'''
Quest:
    Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
    Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

    Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Solution:
    - use two pointers to store the first and second elements in the triplet
    - the way it works is not like "first" gonna store the min, "second" stores the medium
        it's more like a indicator, whenever second exists, it means there must be another number before "second" that
        is smaller than it
'''


class Solution:
    def increasingTriplet(self, nums):
        first, second = float('inf')

        for i in nums:
            if i < first:
                first = i
            elif i < second:
                second = i
            else:
                return True

        return False
