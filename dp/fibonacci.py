# dp: optimized recursion
# characteristics:
#   1. asking for an optimal value (min or max), number of ways to do somethings
#       1.1 min cost
#       1.2 max profit
#       1.3 how many ways
#       1.4 longest possible
#   2. at each step, make a decision that affects future decisions - different from greedy (always take local max)
#       2.1 pick between two elements
#       2.2 affect future decisions: if you pick x, you can't pick y in next step
# state: set of variables that can fully define a scenario
#   1. index along input string, array, number
#   2. a second index: define right-closing boundary
#   3. numeriical constraints: k. allowed obstacles, etc.
#   4. boolean to represent a status
# Time Complexity: O(N x F), N: number of total states, F: time to compute each state. N = multi(all dimensions)
# Space Complexity: O(N). Some bottom-up can be optimized
# top-down
#   recursion + memorization (hashmap to store each state), state order doesn't matter
# bottom-up
#   iteration + array (initiazed for every state), state order matters


# problem definition
# Find Fibonacci number given N. F(n) = F(n-1) + F(n-2)

# pure recursion
def recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursion(n - 1) + recursion(n - 2)
# Time complexity: O(2^n) 

# top-down
memo = {}
def topdown(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = topdown(n - 1) + topdown(n - 2)
    return memo[n]
# Time complexity: O(n), each state is computed only once

# bottom-up
def bottomup(n):
    # array
    arr = [0] * (n+1)
    # base case
    arr[1] = 1
    # iteration
    for i in range(2, n+1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]
# Time complexity: O(n)
