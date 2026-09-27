class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # attempt 1. brute force dfs -- TLE (85/88)

        # strategy: starting from either step 0 or 1, choose either to step
        # 1 or 2 steps, and maintain the minimum steps from there

        n = len(cost)

        def attemp1(i):
            if i == n:
                return 0

            if i > n:
                return n + 1

            return min(dfs(i+1), dfs(i + 2)) + cost[i]

        
        # return min(attempt1(0), attempt1(1))


        # attempt 2. memoized dfs -- accepted

        cache = {}

        def attempt2(i):
            if i in cache:
                return cache[i]

            if i == n:
                return 0

            if i > n:
                return n + 1

            cache[i] = min(attempt2(i+1), attempt2(i + 2)) + cost[i]
            return cache[i]

        # return min(attempt2(0), attempt2(1))


        # attempt 3. dp somehow

        # similarily to the other climbing stairs, the ways a position can be reached
        # is the sum of the ways to reach the previous 2 steps, instead of summing the number
        # of ways to reach it, pick the minimum cost

        def attempt3():

            dp = [0] * n

            dp[0] = cost[0]
            dp[1] = cost[1]

            for i in range(2, n):
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

            return min(dp[n-1], dp[n-2]) 

        return attempt3()




        


            

        