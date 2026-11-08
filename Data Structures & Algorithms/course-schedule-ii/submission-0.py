class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i:[] for i in range(numCourses)}

        for course,prereq in prerequisites:
            graph[course].append(prereq)

        result = []

        def dfs(n,path):
            if n in path:
                return False

            path.add(n)

            for neighbor in graph[n]:
                if not dfs(neighbor,path):
                    return False

            path.pop()
            result.append(n)
            graph[n] = []

            return True

        for i in range(numCourses):
            path = set()

            if not dfs(i,path):
                return []

        return result



        