class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        


        def dfs(i,j): # i = row , j = column
            if not (0 <= i < len(grid) and 0 <= j < len(grid[i])):
                return

            if grid[i][j] == "0":
                return

            if (i,j) in visited:
                return

            visited.add((i,j))

            dfs(i-1, j) # top node
            dfs(i+1, j) # bottom node
            dfs(i, j-1) # left node
            dfs(i, j+1) # right node

        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands+=1

        return islands



        


