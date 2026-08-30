class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []


        def dfs(r,c):
            if (r,c) in visited:
                return

            if c == len(heights[r])-1 or r == len(heights)-1:
                oceans.add("A")


            if c == 0 or r == 0:
                oceans.add("P")

            current = heights[r][c]  

            visited.add((r,c))

            if c-1 >= 0 and heights[r][c-1] <= current:
                dfs(r,c-1)

            if r-1 >= 0 and heights[r-1][c] <= current:
                dfs(r-1,c)        

            if c+1 < len(heights[r]) and heights[r][c+1] <= current:
                dfs(r,c+1)

            if r+1 < len(heights) and heights[r+1][c] <= current:
                dfs(r+1,c)

        for r in range(len(heights)):
            for c in range(len(heights[r])):
                visited = set()
                oceans = set()
                dfs(r,c)
                if len(oceans) == 2 :
                    res.append([r,c])

        return res

        

            