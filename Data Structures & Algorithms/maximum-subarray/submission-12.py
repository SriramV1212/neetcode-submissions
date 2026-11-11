class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left  = 0
        right = 0

        res = nums[left]
        total = 0

        while right < len(nums):
            if nums[right] > total and total < 0:
                left = right
                total = nums[right]
            else:
                total+=nums[right]

            
            res = max(res,total)
            right+=1

        return res


        