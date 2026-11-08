class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i:[] for i in range(numCourses)}

        for course,prereq in prerequisites:
            graph[course].append(prereq)

        result = []
        visited = set()

        def dfs(n,path):
            if n in path:
                return False

            if n in visited:
                return True

            path.add(n)

            for neighbor in graph[n]:
                if not dfs(neighbor,path):
                    return False

            path.remove(n)
            visited.add(n)
            result.append(n)

            return True

        for i in range(numCourses):
            if i not in visited:
                path = set()

                if not dfs(i,path):
                    return []

        return result



        