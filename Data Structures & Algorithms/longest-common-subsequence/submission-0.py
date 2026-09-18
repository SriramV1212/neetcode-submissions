class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # dp = [[-1] * len(text1) for _ in range(len(text2))]
        dp = {}

        def recurse(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if i == len(text1) or j == len(text2):
                return 0

            dp[(i,j)] = 1 + recurse(i+1,j+1) if text1[i] == text2[j] else max(recurse(i+1,j),recurse(i,j+1))

            return dp[(i,j)]

        return recurse(0,0)


        