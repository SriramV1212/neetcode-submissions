class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for _ in range(m)]

        def recurse(r,c):
            if r>=m or c>=n:
                return 0

            if dp[r][c] != 0:
                return dp[r][c]

            if r == m-1 and c == n-1:
                return 1

            dp[r][c] = recurse(r+1,c) + recurse(r,c+1)

            return dp[r][c]

        return recurse(0,0)

            
        