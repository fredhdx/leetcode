##You are given a 0-indexed array nums of n integers, and an integer k.
##
##The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
##
##Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
##
##The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.


def getAverages(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    average = [-1] * n
    
    window_size = 2 * k + 1
    
    if window_size > n:
        return average
    
    window_sum = 0
    for i in range(window_size):
        window_sum += nums[i]
        
    average[k] = window_sum // window_size
    
    for i in range(window_size, n):
        window_sum += nums[i] - nums[i - window_size]
        average[i - k] = window_sum // window_size
        
    return average
    
def getAverages(nums: List[int], k: int) -> List[int]:
        n = len(nums)
        div = 2*k + 1
        ans = [-1] * n

        if n < 2*k + 1:
            return ans

        prefix = [ nums[0] ]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        for i in range(k, n - k):
            ans[i] = (prefix[i + k] - prefix[i - k] + nums[i - k]) // div

        return ans
