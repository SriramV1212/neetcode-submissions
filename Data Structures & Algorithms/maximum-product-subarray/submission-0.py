class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]

        dp = [[float("inf"),float("inf")] for _ in range(len(nums))]


        def recurse(idx):
            nonlocal ans
            if dp[idx]!= [float("inf"),float("inf")]:
                return dp[idx]
            
            if idx == 0:
                dp[idx][0] = nums[idx]
                dp[idx][1] = nums[idx]
                return dp[idx]

            dp[idx-1] = recurse(idx-1)
            min_val = dp[idx-1][0]
            max_val = dp[idx-1][1]

            dp[idx][0] = min(nums[idx], nums[idx] * min_val, nums[idx] * max_val)
            dp[idx][1] = max(nums[idx], nums[idx] * min_val, nums[idx] * max_val)

            ans = max(ans,dp[idx][1])

            return dp[idx]

        recurse(len(nums)-1)
        return ans
        