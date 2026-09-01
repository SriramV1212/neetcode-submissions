class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        graph = defaultdict(list)

        for key, value in edges:
            graph[key].append(value)
            graph[value].append(key)

        visited = set()

        def dfs(n, parent):
            if n in visited:
                return False 

            visited.add(n)

            for neighbor in graph[n]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, n):
                    return False

            return True


        return dfs(0,-1) and len(visited) == n

        






        