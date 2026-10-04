class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # attempt 1. (already solved but just doing it again for fun) dfs

        def attempt1():

            g = {i: [] for i in range(n)}
            for a, b in edges:
                g[a].append(b)
                g[b].append(a)

            seen = set()

            def dfs(a, parent):
                if a in seen:
                    return False

                seen.add(a)
                if not g[a]:
                    return True

                for b in g[a]:
                    if b != parent:
                        if not dfs(b, a):
                            return False
                return True
            
            if not dfs(0, -1):
                return False

            return len(seen) == n
        
        return attempt1()

            


