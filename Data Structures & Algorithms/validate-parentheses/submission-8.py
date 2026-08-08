class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'(':')', '{':'}','[':']'}

        stack = []

        for x in s:
            if x in brackets:
                stack.append(x)
            elif stack and x == brackets[stack[-1]]:
                stack.pop()
            else:
                return False


        return stack == []






        