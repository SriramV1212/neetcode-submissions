class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        current_sum = float("-inf")
        max_sum = float("-inf")


        for i in range(len(nums)):
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
            else:
                current_sum+=nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum


            


            
            




        