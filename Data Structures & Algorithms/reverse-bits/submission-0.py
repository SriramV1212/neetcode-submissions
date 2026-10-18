class Solution:
    def reverseBits(self, n: int) -> int:

        l = []

        binary = bin(n)[2:]

        for bit in range(len(binary)-1,-1,-1):
            l.append(binary[bit])

        remaining = 32 - len(binary)

        for _ in range(remaining):
            l.append("0")

        number = "".join(l)

        return int(number,2)
        