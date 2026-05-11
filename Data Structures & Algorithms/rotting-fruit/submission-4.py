class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        q = []
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1


        layer = 0
        while q and fresh > 0:
            l = len(q) 
            for _ in range(l):
                x, y = q.pop(0)

                for dx, dy in dirs:
                    r, c = x + dx, y + dy
                    if ((r) in range(m) and (c) in range(n)):
                        if grid[r][c] == 1:
                            q.append((r, c))
                            grid[r][c] = 2
                            fresh-=1
                        

            layer += 1

        return layer if fresh == 0 else -1
