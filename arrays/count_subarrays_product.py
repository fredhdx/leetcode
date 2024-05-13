#Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

def find_count(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    left = ans = 0
    curr = 1

    for right in range(len(nums)):
        curr *= nums[right]

        while curr >= k:
            curr \\= nums[left]
            left += 1

        # number of arrays ending at right
        ans += right - left + 1 

    return ans
        

