'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i in range(len(nums) - 2): # anchoring i
            print i
            if i > 0 and nums[i] == nums[i - 1]: # check if i and i - 1 are the same, if true, skip this round
                continue

            low_bond, up_bond = i + 1, len(nums) - 1
            while low_bond < up_bond:
                sum = nums[i] + nums[low_bond] + nums[up_bond]
                if sum == 0:
                    res.append([nums[i], nums[low_bond], nums[up_bond]])
                    while low_bond < up_bond and nums[low_bond] == nums[low_bond + 1]: # check if low_bond and low_bond + 1 are the same, if true, skip this low_bond + 1
                        low_bond += 1
                    while low_bond < up_bond and nums[up_bond] == nums[up_bond - 1]: # check if up_bond and up_bond - 1 are the same, if true, skip this up_bond - 1
                        up_bond -= 1
                    low_bond += 1
                    up_bond -= 1
                elif sum < 0:
                    low_bond += 1
                else:
                    up_bond -= 1

        return res

test = Solution()

x = [-1,0,1,2,-1,-4]
print(test.threeSum(x))