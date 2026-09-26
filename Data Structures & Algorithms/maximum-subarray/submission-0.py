class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0


        for i in range(len(nums)):
            if nums[i] > sum:
                sum = nums[i]
                continue

            sum+=nums[i]

        return sum


            


            
            




        