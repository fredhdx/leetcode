# problem definition
# You are planning to rob houses along a street. The ith house has nums[i] money. If you rob two houses beside each other, the alarm system will trigger and alert the police. What is the most money you can rob without alerting the police?
# Input: values, i
# output: maximized total robbed money
# formulation: consider up to ith house (i is the index)
#   two cases:
#       1. if we have robbed i-1, then we can't rob i. So total(i) = total(i-1)
#       2. if we haven't robbed i-1, then we must robbed i-2, so total(i) = total(i-2) + values[i]
#   base cases:
#       1. if there is only 1 house (i=0): get values[0]
#       2. if there are two houses (i=1): get max(values[0], values[1])
#   final formulation: total(i) = max(total(i-1), total(i-2) + values[i])
#

from functools import cache

# topdown

@cache
def topdown(nums, i):
    if i == 0:
        return nums[0]
    if i == 1:
        return max(nums[0], nums[1])

    return  max(topdown(nums, i-1), topdown(nums, i-2) + nums[i])


# bottomup
def bottomup(nums, i):
    n = len(nums)

    if n == 1:
        return nums[0]

    arr = [ 0 ] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    back_two = nums[0]
    back_one = max(nums[0], nums[1])

    for i in range(2, n):
        back_two = back_one
        back_one = max(back_one, back_two + nums[i])

    return back_one
