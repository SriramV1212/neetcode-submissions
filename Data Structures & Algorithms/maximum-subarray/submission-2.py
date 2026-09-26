class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0


        for i in range(len(nums)):
            if nums[i] > sum + nums[i]:
                sum = nums[i]
            else:
                sum+=nums[i]

        return sum


            


            
            




        