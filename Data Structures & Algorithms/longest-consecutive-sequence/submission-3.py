class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        res = 0

        for n in nums:
            if n-1 not in numset:
                streak = 1
                i=n
                while i+1 in numset:
                    streak+=1
                    i+=1
                res = max(res,streak)
        
        return(res)

        



        
        