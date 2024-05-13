# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# dp(i) returns the LIS ends with ith element
# dp(i) = max(dp(j) + 1 for all j < i and nums[i] > nums[j])


# find the maximum LIS ending at ith element
def topdown(nums, i):
    # base case
    ans = 1

    for j in range(i):
        if nums[i] > nums[j]:
            ans = max(ans, topdown(nums, j) + 1)

    return ans

return max(dp(nums, i) for i in range(len(nums)))


def bottomup(nums):
    n = len(nums)
    arr = [ 1 ]  * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                arr[i] = max(arr[i], arr[j] + 1)

    return max(arr)


