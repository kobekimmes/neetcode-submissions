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


        # attempt 2. memoized dfs

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

        return min(attempt2(0), attempt2(1))
        


            

        