class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def backtrack(i,path):
            if i == len(s):
                res.append(path.copy())
                return

            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    path.append(s[i:j+1])
                    backtrack(j+1,path)
                    path.pop()

        backtrack(0,[])

        return res

        


    def isPalindrome(self,string,left,right):

        while left < right:
            if not string[left] == string[right]:
                return False

            left+=1
            right-=1

        return True

    


            

        
        