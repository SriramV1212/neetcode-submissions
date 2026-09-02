class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(n,path):
            if n in path:
                return

            path.add(n)
            visited.add(n)

            for neighbor in graph[n]:
                dfs(neighbor,path)

        components = 0

        for node in range(n):
            if not node in visited:
                path = set()
                dfs(node,path)
                components+=1

        return components


        