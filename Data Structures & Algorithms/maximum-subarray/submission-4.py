class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        sum = float("-inf")
        max_sum = float("-inf")


        for i in range(len(nums)):
            if nums[i] > sum + nums[i]:
                sum = nums[i]
            else:
                sum+=nums[i]

            max_sum = max(max_sum, sum)

        return max_sum


            


            
            




        