class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [0] * len(nums)


        res = 1


        def recurse(idx):

            if dp[idx] != 0:
                return dp[idx]

            if idx == len(nums)-1:
                dp[idx] = 1
                return dp[idx]

            
            max_length = 1


            for i in range(idx+1, len(nums)):
                if nums[i] > nums[idx]:
                    length = 1 + recurse(i)
                    max_length = max(length,max_length)

            
            dp[idx] = max_length
            return dp[idx]

        for i in range(len(nums)):
            length = recurse(i)

            res = max(res,length)

        return res

        



        