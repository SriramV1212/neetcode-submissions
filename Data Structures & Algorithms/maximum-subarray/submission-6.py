class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]


        for i in range(len(nums)):
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
            else:
                current_sum+=nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum


            


            
            




        