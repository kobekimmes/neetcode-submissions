class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # attempt 1. brute force dfs -- TLE (24/26)

        # strategy: starting from each cell, perform a 
        # search outward from each cell, if its strictly
        # greater than the previous cell, add it to a 
        # running sum of the paths current length, 
        # otherwise end the search in that direction

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        n, m = len(matrix), len(matrix[0])

        def attempt1(i, j, prev):

            if 0 <= i < n and 0 <= j < m:

                curr = matrix[i][j]
                if curr <= prev:
                    return 0

                best = 0
                for dx, dy in dirs:
                    best = max(best, 1 + attempt1(i + dx, j + dy, curr))

                return best

            else:
                return 0
        
        # best = 0
        # for i in range(n):
        #     for j in range(m):
        #         best = max(best, attempt1(i, j, -1))
        # return best

        # attempt 2. memoized dfs

        # store positions in a cache, mapping
        # to the longest path up to that point

        cache = {}

        def attempt2(i, j, prev):

            if 0 <= i < n and 0 <= j < m:

                curr = matrix[i][j]
                if curr <= prev:
                    return 0

                if (i, j) in cache:
                    return cache[(i, j)]

                best = 0
                for dx, dy in dirs:
                    best = max(best, 1 + attempt2(i + dx, j + dy, curr))

                cache[(i, j)] = best
                return best
            else:
                return 0
        
        best = 0
        for i in range(n):
            for j in range(m):
                best = max(best, attempt2(i, j, -1))
        return best





            
            