class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        for n in nums:
            product*=n

        res = []

        for n in nums:
            res.append(product/n)

        return(res)
