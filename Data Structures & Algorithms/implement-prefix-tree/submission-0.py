class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = [None] * 26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root

        for ch in word:
            nxt = cur.children[ord(ch)-97]
            if not nxt:
                new = TrieNode(ch)
                cur.children[ord(ch)-97] = new
                cur = new
            else:
                cur = nxt
        
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            nxt = cur.children[ord(ch)-97]
            if nxt:
                cur = nxt
            else:
                return False
        
        if cur.end:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for ch in prefix:
            nxt = cur.children[ord(ch)-97]
            if nxt:
                cur = nxt
            else:
                return False
        return True
        
        