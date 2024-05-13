#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

def longestOnes(nums: List[int], k: int) -> int:
    left = curr = ans = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
        
    return ans
