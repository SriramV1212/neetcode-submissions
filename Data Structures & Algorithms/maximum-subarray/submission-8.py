class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left  = 0
        right = 0

        res = 0

        while right < len(nums):
            if nums[right] > res:
                left = right
                res = nums[right]
                right+=1

            res+=nums[right]
            right+=1

        return res
        