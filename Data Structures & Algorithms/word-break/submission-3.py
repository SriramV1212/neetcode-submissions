class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True

        def recurse(idx):
            if idx in dp:
                return dp[idx]

            if idx == len(s):
                return dp[idx]

            for string in wordDict:
                if s[idx:].startswith(string) and recurse(idx + len(string)):
                    dp[idx] = True
                    return True
            dp[idx] = False
            return False

        return recurse(0)

                


        