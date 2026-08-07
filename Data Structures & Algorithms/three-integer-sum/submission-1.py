class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            a=nums[i]
            
            if a>0:
                break

            if i>0 and a==nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                target = a + nums[left] + nums[right]

                if target < 0:
                    left+=1

                elif target > 0:
                    right-=1

                else:
                    res.append([a,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left>0 and nums[left]!=nums[left-1]:
                        left+=1
        
        return res


            

        

        