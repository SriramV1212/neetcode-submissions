class Solution:
    def checkValidString(self, s: str) -> bool:

        stack_b = []

        stack_a = []

        for i,char in enumerate(s):
            
            if char == "(":
                stack_b.append([char,i])

            if char == "*":
                stack_a.append([char,i])

            if char == ")":
                if stack_b:
                    stack_b.pop()
                elif stack_a:
                    stack_a.pop()
                else:
                    return False

        
        while stack_a and stack_b:
            if stack_b[-1][1] < stack_a[-1][1]:
                stack_a.pop()
                stack_b.pop()
            else:
                return False

        if stack_b:
            return False
        else:
            return True





        