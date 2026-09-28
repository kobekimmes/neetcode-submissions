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

        # attempt 2. memoized dfs

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
        
        return attempt2(0, 0)



        