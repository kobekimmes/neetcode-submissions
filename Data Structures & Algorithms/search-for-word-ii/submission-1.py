class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def backtrack(node, board, cur_x, cur_y, result):

            if 0 <= cur_y < len(board) and 0 <= cur_x < len(board[cur_y]):
                ch = board[cur_y][cur_x]

                key = ord(ch) - 97
                if ch == "#":
                    return

                child = node.children[key]

                if not child:
                    return

                if child.word:
                    result.append(child.word)
                    child.word = None
            
                board[cur_y][cur_x] = '#'

                for dx, dy in self.dirs:
                    backtrack(child, board, cur_x + dx, cur_y + dy, result)  

                board[cur_y][cur_x] = ch


        trie = Trie()
        for word in words:
            trie.add(word)

        result = []

        for r in range(len(board)):
            for c in range(len(board[r])):
                backtrack(trie.root, board, c, r, result)

        return result



# Snag from the last problem
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):

        curr = self.root
        for ch in word:
            i = ord(ch) - 97

            if not curr.children[i]:
                new = TrieNode()
                curr.children[i] = new
                curr = new
            else:
                curr = curr.children[i]
        curr.word = word
        

    def add_rec(self, curr, word, i):
        if i == len(word):
            curr.word = word
            return

        key = ord(word[i]) - 97

        if not curr.children[key]:
            curr.children[key] = TrieNode()

        self.add_rec(curr.children[key], word, i+1)


    def check(self, curr, word, i):
        if i == len(word):
            return curr.end

        if word[i] == '.':
            for child in curr.children:
                if child:
                    if self.check(child, word, i+1):
                        return True
            return False

        else:
            key = ord(word[i]) - 97
            if not curr.children[key]:
                return False
            return self.check(curr.children[key], word, i+1)


class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.word = None