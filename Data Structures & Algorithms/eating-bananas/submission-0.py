class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        r = max(piles)
        l = 1
        min_k = 0

        while l<=r:
            k = (l+r)//2

            if self.isValid_k(piles,k,h):
                min_k = k
                r = k-1
            else:
                l = k+1

        return min_k

    
    def isValid_k(self,piles,k,h):

        hours = 0

        for pile in piles:
            hours+=math.ceil(pile/k)

        if hours<=h:
            return True
        else:
            return False







        