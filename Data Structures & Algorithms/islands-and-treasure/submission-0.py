class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        INF = (2 ** 31) - 1
        q = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q += [(i, j)]
        level = 0         
        while q:
            l = len(q)
            for _ in range(l):
                x,y = q.pop(0)

                if x >= m or y >= n or x < 0 or y < 0:
                    continue

                for d in dirs:
                    if not (x + d[0] >= m or y + d[1] >= n or x + d[0] < 0 or y + d[1] < 0) and grid[x+d[0]][y+d[1]] == INF:
                        q += [(x + d[0], y + d[1])]

                grid[x][y] = min(level, grid[x][y])
            level+=1

                
                
                

                



                        

                        

                        


            


            

