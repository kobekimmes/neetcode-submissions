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

        # attempt 2. memoized dfs -- accepted

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

        # return dfs(0)

        # attempt 3. dp somehow -- accepted 

        # strategy: reaching the nth step has 2 ways, we can either reach it from
        # the n-1th step by stepping 1 step, or the n-2nd step by stepping 2 steps.
        # at any step n, the way to reach it is the sum of the ways to reach the 2
        # preceding steps. 


        def attempt3():
            dp = [0] * (n+1)

            # we can reach both the first and second step in 1 move
            dp[0] = 1
            dp[1] = 1

            for i in range(2, n+1):

                dp[i] = dp[i - 1] + dp[i - 2]

            return dp[n]
        
        # return attempt3()

        # attempt 4. dp space optimized

        # we can observe that we really only care about the 2 preceding values, 
        # and meaning we don't need to maintain the entire array in memory but
        # instead with just 2 pointer values

        def attempt4():
            
            prev1 = 1
            prev2 = 1
            curr = 1

            for i in range(2, n+1):
                curr = prev1 + prev2
                prev2 = prev1
                prev1 = curr

            return curr

        return attempt4()










