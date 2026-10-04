class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def build_undir_graph(v, e):
            g = {i: [] for i in range(v)}
            for a, b in e:
                g[a].append(b)
                g[b].append(a)

            return g

        # attempt 1. (already solved but just doing it again for fun) dfs

        def attempt1():

            g = build_undir_graph(n, edges)
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
        
        # return attempt1()

        # attempt 2. bfs

        from collections import deque

        def attempt2():

            g = build_undir_graph(n, edges)
            seen = set()
            q = deque()
            q.appendleft((0, -1))

            while q:

                a, parent = q.popleft()

                if a in seen:
                    return False

                seen.add(a)

                for b in g[a]:
                    if b != parent:
                        q.append((b, a))

            return len(seen) == n
        
        return attempt2()




            

            


