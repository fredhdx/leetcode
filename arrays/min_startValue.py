#Given an array of integers nums, you start with an initial positive value startValue.
#
#In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#
#Return the minimum positive value of startValue such that the step by step sum is never less than 1.

def minStartValue(nums: List[int]) -> int:
    curr = nums[0]
    ans = curr
    for i in range(1, len(nums)):
        curr += nums[i]
        ans = min(ans, curr)
        
    if ans >= 1:
        return 1
    else:
        return 1-ans
