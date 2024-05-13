#Example 3: Given an integer array nums, find all the numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

def solution(nums: List[int]) -> List[int]:
    ans = []
    myset = set(nums)  # O(1) check
    
    for x in myset:
        if (x+1) not in myset and (x-1) not in myset:
            ans.append(x)

    return ans
