class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product , zer_count = 1,0

        res=[]

        for n in nums:
            if n==0:
                zer_count+=1
                continue
            product*=n

        if zer_count > 1:
            return([0] * len(nums))

        if zer_count == 1:
            for i in range(len(nums)):
                if nums[i]==0:
                    res.append(product)
                    continue
                res.append(0)
            
            return(res)
        
        for n in nums:
            res.append(product//n)
        
        return(res)

        



        

