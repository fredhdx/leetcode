#Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

def find_sum(nums: List[int], k: int) -> int:

    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr = curr - nums[i-k] + nums[i]
        ans = max(ans, curr)

    return ans



