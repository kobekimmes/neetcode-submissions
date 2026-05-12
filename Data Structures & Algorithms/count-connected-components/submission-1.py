class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def dfs(i):
            if i in seen:
                return 

            seen.add(i)
            for j in graph[i]:
                dfs(j)

        comps = 0
        for i in range(n):
            if i not in seen:
                comps += 1
                dfs(i)

        return comps