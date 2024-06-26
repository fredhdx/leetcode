# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    left = 0
    right = n - 1

    result = [0] * n

    for i in range(n-1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            square = nums[left]
            left += 1
        else:
            square = nums[right]
            right += 1
    
        result[i] = sqaure * square

    return result


