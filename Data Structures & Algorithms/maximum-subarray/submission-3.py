class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        sum = 0
        max_sum = 0


        for i in range(len(nums)):
            if nums[i] > sum + nums[i]:
                sum = nums[i]
            else:
                sum+=nums[i]

            max_sum = max(max_sum, sum)

        return max_sum


            


            
            




        