class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return(0)

        l = 0
        r = 0
        max_length = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                see.remove(s[l])
                l+=1

            seen.add(s[r])
            length = r-l+1
            max_length = max(length, max_length)

            r+=1

        return max_length

            

