class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        partitions = []

        def dfs(i):  # dfs(i) means explore all partitions starting from index i, given everything before i is already partitioned
            if i >= len(s):
                result.append(partitions.copy())
                return

            
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    partitions.append(s[i:j+1])
                    dfs(j+1)
                    partitions.pop()

        
        dfs(0)

        return result


    def isPalindrome(self, s, left, right):
        
        while left < right:
            if s[left]!=s[right]:
                return False

            left , right = left+1, right-1

        return True
        





            



        