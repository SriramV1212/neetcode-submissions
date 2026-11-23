class Solution:
    def checkValidString(self, s: str) -> bool:

        stack_b = []

        stack_a = []

        for char in s:
            
            if char == "(":
                stack_b.append(char)

            if char == "*":
                stack_a.append(char)

            if char == ")":
                if stack_b:
                    stack_b.pop()
                elif stack_a:
                    stack_a.pop()
                else:
                    return False

        
        while stack_a and stack_b:
            stack_b.pop()
            stack_a.pop()

        if stack_b:
            return False
        else:
            return True





        