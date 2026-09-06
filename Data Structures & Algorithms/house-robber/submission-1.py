class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

      

        def recurse(house):
            if dp[house] != -1:
                return dp[house]

            if house <= 1:
                return nums[house]

            dp[house] = max(recurse(house-1), nums[house] + recurse(house-2))
            return dp[house]

        recurse(len(nums)-1)
        recurse(len(nums)-2)


        amt = max(dp)

        return amt