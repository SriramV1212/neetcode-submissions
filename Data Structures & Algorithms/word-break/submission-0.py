class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True

        def recurse(idx):
            nonlocal s
            if idx in dp:
                return dp[idx]

            if idx == len(s):
                return dp[idx]

            for string in wordDict:
                if s[idx:].startswith(s) and recurse(idx + len(s)):
                    dp[idx] = True
                    return True

            return False

        return recurse(0)

                


        