# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def solution1(nums: List[int]) -> int:
    missing = len(nums)
    for i, x in enumerate(nums):
        missing ^= i ^ x

    # i= [0, 1, 2, 3, 4]
    # x=[1, 2, 3, 4, 5]
    # (5 ^ 5) ^ (1^1) ^ (2^2) ^ (3^3) ^ (4^4) ^ 0
    # 0 ^ 0 ^ 0 ^ 0 ^ 0 ^ 0
    # 0 ^ 0
    # 0
    return missing

def solution2(nums: List[int]) -> int:
    myset = set(nums)
    for x in range(len(nums)+1):
        if x not in myset:
            return x
