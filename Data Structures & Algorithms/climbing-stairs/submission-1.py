class Solution:
    def climbStairs(self, n: int) -> int:

        # attempt 1. brute force dfs bottom up -- TLE (24/25)

        def dfs(i):
            if i > n:
                return 0

            if i == n:
                return 1

            return dfs(i + 1) + dfs(i + 2)
        
        # return dfs(0)

        # attempt 2. memoized dfs

        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i > n:
                return 0

            if i == n:
                return 1

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
            
        return dfs(0)