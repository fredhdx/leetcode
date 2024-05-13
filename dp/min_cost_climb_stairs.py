# problem definition
# You are given an integer array cost where cost[i] is the cost of the ith step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor (outside the array, not the last index of cost).
# Input: cost
# formulation: find_min(n) = min(find_min(n-1) + cost[n-1], find_min(n-2) + cost[n-2]), base: find_min(0) = 0, find_min(1) = 0

from typing import List

# topdown
memo = {}
def topdown(cost: List[int], n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0

    if n in memo:
        return memo[n]

    memo[n] = min(topdown(arr, n-1) + cost[n-1], topdown(arr, n-2) + cost[n-2])
    return memo[n]
# topdown(cost, len(cost))

# bottomup
def bottomup(cost: List[int]) -> int:
    arr = [0] * (len(cost) + 1)

    for i in range(2, len(cost) + 1):
        arr[i] = min(arr[i-1] + cost[i-1], arr[i-2] + cost[i-2])

    return bottomup[len(cost)]

