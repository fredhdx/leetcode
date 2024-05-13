#Given an array of integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum (the sum of their individual digits). Return -1 if there is no pair of numbers with the same digit sum.


def solution(nums: List[int]) -> int:

    def digit_sum(num):
        _sum = 0
        while num:
            _sum += num % 10
            num //= 10
        return _sum

    curr = {}
    ans = -1
    for num in nums:
        dsum = digit_sum(num)
        if dsum in curr:
            ans = max(ans, num + curr[dsum])

        curr[dsum] = max(curr[dsum], num)

    return ans



