class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        flag = False
        for n in nums:
            if n==0:
                flag = True
                continue
            product*=n

        res = []

        for n in nums:
            if flag & n==0:
                res.append(product)
                continue

            if flag & n!=0:
                res.append(0)
                continue

            res.append(product//n)

        return(res)
