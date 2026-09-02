class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(n):
            if n in visited:
                return


            visited.add(n)

            for neighbor in graph[n]:
                dfs(neighbor)

        components = 0

        for node in range(n):
            if not node in visited:
                dfs(node)
                components+=1

        return components


        