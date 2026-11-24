class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        path = []
        res = []

        def backtrack(stack,open_b,close_b):
            if len(path) == 2*n:
                res.append("".join(path))
                return

            
            if stack and close_b<n:
                stack.pop()
                path.append(")")
                backtrack(stack,open_b,close_b+1)
                path.pop()
                stack.append("(")
            
            if open_b<n:
                stack.append("(")
                path.append("(")
                backtrack(stack,open_b+1,close_b)
                path.pop()
                stack.pop()

        backtrack([],0,0)

        return res

        

                    

            

                



            
        