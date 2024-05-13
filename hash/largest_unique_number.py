#Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.


def largestUniqueNumber(nums: List[int]) -> int:
    count = {}
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    
    ans = -1
    for n in count:
        if count[n] == 1:
            ans = max(ans, n)
        
    return ans
