class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return("")

        t_map = {}

        for char in t:
            t_map[char] = 1 + t_map.get(char,0)
        
        res = [-1,-1]
        res_len = float("infinity")

        s_map = {}
        l = 0
        need = len(t_map)
        have = 0

        for r in range(len(s)):
            c = s[r]

            s_map[c] = 1 + s_map.get(c,0)

            if c in t_map and s_map[c] == t_map[c]:
                have+=1

            while have==need:
                if (r-l+1) < res_len:
                    res = [l ,r]
                    res_len = r-l+1

                s_map[s[l]]-=1

                if s[l] in t_map and s_map[s[l]]!=t_map[s[l]]:
                    have-=1

                l+=1

        l , r = res

        return(s[l:r+1]) if res_len != float("infinity") else ""


            


        