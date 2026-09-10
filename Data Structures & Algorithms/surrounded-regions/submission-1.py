class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(i, j):

            if i < len(board) and i >= 0 and j < len(board[i]) and j >= 0:

                if board[i][j] == 'O':
                    board[i][j] = "M"

                    for di, dj in ((i + 1, j), (i-1, j), (i, j+1), (i, j-1)):
                        dfs(di, dj)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[i])-1)

        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'M':
                    board[i][j] = 'O'

