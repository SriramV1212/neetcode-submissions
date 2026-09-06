class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]


        dp1 = [-1] * (len(nums)-1)
        dp2 = [-1] * (len(nums)-1)
        

        def recurse(house:int, l:list, dp:list):
            if dp[house] != -1:
                return dp[house]

            if house == 0:
                dp[house] = l[0]
                return dp[house]

            if house == 1:
                dp[house] = max(l[0],l[1])
                return dp[house]

            
            dp[house] = max(recurse(house-1, l, dp), recurse(house-2, l, dp) + l[house])

            return dp[house]

        
        return max(recurse(len(nums)-2, nums[1:], dp1), recurse(len(nums)-2, nums[:-1], dp2))

        