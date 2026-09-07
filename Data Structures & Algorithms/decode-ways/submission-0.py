class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1

        dp = [-1] * len(s)
        dp[0] = 1

        def recurse(idx):

            if dp[idx]!=-1:
                return dp[idx]

            if idx == 0:
                return 1

            if idx == 1:
                temp = 0

                if s[idx]!='0':
                    temp+=1
                if 10 <= int(s[idx-1:idx+1]) <= 26:
                    temp+=1

                dp[idx] = temp

                return temp

            recurse(idx-1)
            recurse(idx-2)

            temp = 0

            if s[idx]!='0':
                temp = dp[idx-1]
 

            if 10 <= int(s[idx-1:idx+1]) <= 26:
                temp = temp + dp[idx-2]
                
            dp[idx] = temp

            return dp[idx]

        return recurse(len(s)-1)

            
            

            






        