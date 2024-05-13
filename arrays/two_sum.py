# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):
    recorded = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in recorded:
            return [i, recorded[complement]]
        else:
            recorded[nums[i]] = i

    raise 'no solution found.'
    
