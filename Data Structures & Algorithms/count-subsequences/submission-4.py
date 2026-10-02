class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # attempt 1. brute force dfs -- TLE (23/25)

        # strategy: keep 2 pointer, i and j, where i points to a character in
        # s and j points to character in t. if s[i] == t[j] increment both ptrs
        # otherwise, increment only i. once you reach the end of j return 1 if 
        # you reach the end of i first, return 0. at each index of s, make the
        # choice to either include in subsequence or skip

        n, m = len(s), len(t)

        if n < m:
            return 0

        def attempt1(i, j):
            if j == m:
                return 1

            if i == n:
                return 0

            subseq = 0
            if s[i] == t[j]:
                subseq += attempt1(i + 1, j + 1)

            subseq += attempt1(i + 1, j)
            return subseq

        # return attempt1(0, 0)

        # attempt 2. memoized dfs -- accepted

        cache = {}

        def attempt2(i, j):
            if j == m:
                return 1

            if i == n:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            subseq = 0
            if s[i] == t[j]:
                subseq += attempt2(i + 1, j + 1)

            subseq += attempt2(i + 1, j)
            cache[(i, j)] = subseq
            return subseq

        # return attempt2(0, 0)

        # attempt 3. dp somehow

        # strategy: 

        def attempt3():

            dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

            for i in range(n+1):
                dp[i][m] = 1

            for i in range(n, -1, -1):
                for j in range(m, -1, -1):
                    if i < n:
                        dp[i][j] = dp[i+1][j]
                        if j < m and s[i] == t[j]:
                            dp[i][j] += dp[i+1][j+1]

            return dp[0][0]

        return attempt3()
            



            

            