#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
#Return the running sum of nums.

def running_sum(nums: List[int]):
    prefix = [ nums[0] ]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    return prefix
