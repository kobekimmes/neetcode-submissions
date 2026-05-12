class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        
        self.trie.add_rec(self.trie.root, word, 0)

    def search(self, word: str) -> bool:
        return self.trie.check(self.trie.root, word, 0)


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
        curr.end = True
        

    def add_rec(self, curr, word, i):
        if i == len(word):
            curr.end = True
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
        self.end = False

    


