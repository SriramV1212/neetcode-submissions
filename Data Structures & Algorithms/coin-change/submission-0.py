class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def recurse(target):
            if target < 0:
                return float("inf")

            if target in dp:
                return dp[target]

            if target == 0:
                return 0

            min_coins = float("inf")

            for coin in coins:
                number = 1 + recurse(target-coin)
                if number < min_coins:
                    min_coins = number

            dp[target] = min_coins
            return min_coins

        ans = recurse(amount)

        if ans == float("inf"):
            return -1
        else:
            return ans
        