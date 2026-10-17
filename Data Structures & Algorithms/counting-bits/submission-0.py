class Solution:
    def countBits(self, n: int) -> List[int]:

        result = []

        for num in range(n+1):

            mask = 1
            count = 0

            while mask <= n:

                if num & mask != 0:
                    count+=1

                mask <<= 1

            
            result.append(count)
        
        return result