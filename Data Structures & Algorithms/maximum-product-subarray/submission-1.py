class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_val = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            temp = min(nums[i], nums[i] * min_val, nums[i] * max_val)
            max_val = max(nums[i], nums[i] * min_val, nums[i] * max_val)
            min_val = temp

            ans = max(ans,max_val)

        return ans

        