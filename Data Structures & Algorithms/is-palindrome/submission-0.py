class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []

        for char in s:
            if char!="":
                forward.append(char)
        
        backward = []

        for i in range(len(s-1),-1,-1):
            if s[i]!="":
                backward.append(s[i])

        return ("".join(forward) == "".join(backward))
        