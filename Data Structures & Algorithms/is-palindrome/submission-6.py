class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []

        for char in s:
            if char!=" " and char.isalnum():
                forward.append(char.lower())
        
        backward = []

        for i in range(len(s)-1,-1,-1):
            if s[i]!=" " and char.isalnum():
                backward.append(s[i].lower)



        return ("".join(forward) == "".join(backward))
        