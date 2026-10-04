class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def build_undir_graph(v, e):
            g = {i: [] for i in range(v)}
            for a, b in e:
                g[a].append(b)
                g[b].append(a)

            return g

        # attempt 1. dfs

        def attempt1():

            g = build_undir_graph(n, edges)
            seen = set()

            def dfs(i):
                if i in seen:
                    return False

                seen.add(i)
                for j in g[i]:
                    dfs(j)

                return True

            cc = 0
            for i in range(n):
                if dfs(i):
                    cc += 1
            return cc

        return attempt1()
            