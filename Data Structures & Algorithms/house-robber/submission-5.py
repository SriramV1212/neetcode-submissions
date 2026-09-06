class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [-1] * len(nums)

        def recurse(house):
            if dp[house] != -1:
                return dp[house]

            if house == 0:
                dp[house] = nums[0]
                return dp[house]

            if house == 1:
                dp[house] = max(nums[0], nums[1])
                return dp[house]

            dp[house] = max(recurse(house-1), nums[house] + recurse(house-2))
            return dp[house]

        recurse(len(nums)-1)

        amt = max(dp)

        return amt