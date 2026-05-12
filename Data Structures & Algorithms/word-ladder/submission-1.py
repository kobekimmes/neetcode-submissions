class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def get_keys(word):
            return [word[:i] + "*" + word[i+1:] for i in range(len(word))]
        
        def build_graph(words):
            g = {}
            for word in words:
                word_keys = get_keys(word)
                for key in word_keys:
                    edges = g.get(key, [])
                    edges.append(word)
                    g[key] = edges
            return g


        g = build_graph(wordList)
        q = [(beginWord, 1)]
        seen = set()

        while q:
            curr, ll = q[0]

            if curr == endWord:
                return ll

            edges = get_keys(curr)

            for edge in edges:
                if edge in g:
                    reconstructed_words = g[edge]
                    for word in reconstructed_words:
                        if word not in seen:
                            q.append((word, ll + 1))
                            seen.add(word) 
            q = q[1:]

        return 0

            







        

       
                
                    


