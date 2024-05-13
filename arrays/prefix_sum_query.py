#Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
#
#For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

def query(nums: List[int], queries: List[List[int, int]], limit:int) -> bool:
    
    if len(nums) == 0:
        return [False]*len(queries)

    prefix_sum = [ nums[0] ]
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i-1])

    ans = []
    size = len(nums)
    for left, right in queries:

        if left < 0 or right > size:
            ans.append(False)
            continue

        curr = prefix_sum[right] - prefix_sum[left] + nums[left]
        ans.append(curr < limit)

    return ans
