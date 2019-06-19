'''
Quest:
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    Note:
    The solution set must not contain duplicate triplets.

    Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

Solution:
    - using collections function? no cause we are not counting how many tuple, we need to know exactly who they are
    - first sort (quick sort)
    - because a + b + c = 0, so -a = b + c, outlet loop fix -a,
        then from (a, max], we try to find if there is b and c satisfy the equation
    - knowing what "continue" does
'''


class Solution:
    def threeSum(self, nums):
        res, N = [], len(nums)
        nums.sort()
        for i in range(N):
            # one duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i + 1, N - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # two duplicate
                    while l < N and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return res


test = Solution()

x = [0, 0, 0]
print(test.threeSum(x))