class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        islands = 0

        def dfs(r,c):

            if not 0 <= r < len(grid):
                return

            if not 0 <= c < len(grid[r]):
                return

            if grid[r][c] == "0":
                return

            if (r,c) in seen:
                return

            seen.add((r,c))

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    dfs(r,c)
                    islands+=1

        return islands


        
        