class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0]<nums[-1]:
            return nums[0]

        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l + r) // 2
            if mid == r:
                return nums[mid]
                break

            if (mid)!= r and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]

            elif mid!=l and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            else:
                l = mid - 1

        



        
        