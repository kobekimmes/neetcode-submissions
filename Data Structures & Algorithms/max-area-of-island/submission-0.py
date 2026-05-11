class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        maxIsland = 0

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            size = 1
            for d in dirs:
                size += dfs(i + d[0], j + d[1])
            
            return size

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxIsland = max(dfs(i, j), maxIsland)
        
        return maxIsland
            


