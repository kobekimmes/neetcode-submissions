class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        self.dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if self.backtrack(0, word, board, c, r):
                    return True
        
        return False



    def backtrack(self, i, target, board, cur_x, cur_y):

        if i >= len(target):
            return True

        if 0 <= cur_y < len(board) and 0 <= cur_x < len(board[cur_y]):

            curr = board[cur_y][cur_x]
            if curr == "#":
                return False
            elif curr == target[i]:
                board[cur_y][cur_x] = '#'
                for dx, dy in self.dirs:
                    if self.backtrack(i+1, target, board, cur_x + dx, cur_y + dy):
                        return True
                board[cur_y][cur_x] = curr
                return False
        return False

        