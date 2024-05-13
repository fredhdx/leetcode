#Example 2: 2270. Number of Ways to Split Array
#
#Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.


def find_split(nums: List[int]):

    prefix = [ nums[0] ] 
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])


    ans = 0
    for i in range(len(nums) - 1):
        left_sum = prefix[i]
        right_sum = prefix[-1] - prefix[i]
        if left_sum >= right_sum:
            ans += 1

    return ans
