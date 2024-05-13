class Solution:
    def twoSum(self, nums, target):
        acc = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in acc:
                return i, acc[res]
            else:
                acc[nums[i]] = i

        return -1, -1