#Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

def solution(nums) -> List[int]:
    counts = {}
    
    for arr in nums:
        for x in arr:
            counts[x] += 1


    n = len(nums)
    ans = []
    for x in counts:
        if counts[x] == n:
            ans.append(x)

    return ans



