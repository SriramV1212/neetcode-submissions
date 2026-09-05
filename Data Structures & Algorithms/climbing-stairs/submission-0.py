class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}

        def recurse(step):
            if step in dp:
                return dp[step]
            
            if step <= 1:
                return 1


            dp[step] = recurse(step-1) + recurse(step-2)

            return recurse(step-1) + recurse(step-2)

        return recurse(n)

        