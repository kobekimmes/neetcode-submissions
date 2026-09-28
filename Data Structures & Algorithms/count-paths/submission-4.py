class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
 
        # attempt 1. brute force dfs -- TLE (20/22)

        def attempt1(i, j):

            if 0 <= i < m and 0 <= j < n:

                if i == m-1 and j == n-1:
                    return 1

                right = attempt1(i, j+1)
                down = attempt1(i+1, j)

                return right + down
            
            return 0
    
        # return attempt1(0, 0)

        # attempt 2. memoized dfs -- accepted but slow

        # maintain the indices in a cache, if we see them
        # again, return early. more formally, the indices,
        # i, j will map to the number of unique paths 
        # available from that location.

        cache = {}

        def attempt2(i, j):

            if 0 <= i < m and 0 <= j < n:

                if (i, j) in cache:
                    return cache[(i, j)]

                if i == m-1 and j == n-1:
                    return 1

                right = attempt2(i, j+1)
                down = attempt2(i+1, j)

                cache[(i, j)] = right + down
                return cache[(i, j)]
            
            return 0
        
        # return attempt2(0, 0)

        # attempt 3. bottom up dp -- accepted beats 100%

        # strategy: starting from 0, 0, populate a dp cache
        # at each (i, j) by summing the number of ways to reach
        # the cell directly above it and directly to the left
        # of it. return the cached value at (m-1, n-1)

        def attempt3():

            dp = [[0 for _ in range(n)] for _ in range(m)]

            # initialize the top rown and leftmost column since
            # for each one of those cells there is at most 1
            # way

            for i in range(m):
                dp[i][0] = 1

            for j in range(n):
                dp[0][j] = 1

            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

            return dp[m-1][n-1]
        
        return attempt3()



        