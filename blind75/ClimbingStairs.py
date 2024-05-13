class Solution:
    def __init__(self, n):
        if n == 1:
            return 1
        
        steps = [0] * (n + 1)
        steps[1] = 1
        steps[2] = 2

        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[-1]

from functools import lru_cache

class Solution2:
    @lru_cache(maxsize=30)
    def helper(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.helper(n - 1) + self.helper(n - 2)

    def __init__(self, n):
        return self.helper(n)