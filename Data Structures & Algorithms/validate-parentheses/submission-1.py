class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'(':')', '{':'}','[':']'}

        b = []

        for x in s:
            if x in brackets:
                b.append(x)
            elif b != [] and x == brackets[b[-1]]:
                b.pop()


        return b == []

        