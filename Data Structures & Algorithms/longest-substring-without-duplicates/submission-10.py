class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        res = 0

        current = set()

        while right < len(s):

            if s[right] in current:
                while s[right] in current and left < len(s):
                    current.remove(s[left])
                    left+=1

            current.add(s[right])

            res = max(len(current),res)
            right+=1

        
        return res


        