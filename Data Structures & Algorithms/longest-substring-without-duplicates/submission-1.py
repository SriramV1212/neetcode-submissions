class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 1


        left = 0
        right = 1

        while right < len(s):
            length = 0
            seen = set()
            if s[left]!= s[right]:
                length+=2
                seen.update([s[left],s[right]])
                right+=1

                while right < len(s) and s[right] not in seen:
                    length+=1
                    seen.add(s[right])
                    right+=1

                max_length = max(max_length,length)
                

            left = right
            right+=1

        return(max_length)


                

        