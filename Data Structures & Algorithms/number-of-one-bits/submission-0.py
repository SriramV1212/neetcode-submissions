class Solution:
    def hammingWeight(self, n: int) -> int:

        mask = 1
        count = 0

        while mask <= n:

            if n & mask != 0:
                count+=1

            mask <<= 1

        return count

        