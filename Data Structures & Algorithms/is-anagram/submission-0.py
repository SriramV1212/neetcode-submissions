class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        for n in s:
            seen_s[n] = seen_s.get(n,0) + 1
        
        for n in t:
            seen_t[n] = seen_t.get(n,0) + 1

        if seen_s == seen_t:
            return True
        else:
            return False



        