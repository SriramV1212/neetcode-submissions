class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mappings = {}



        for s in strs:
            char_map = {}
            for char in s:
                char_map[char] = 0 + char_map.get(char,0)
            key = tuple(sorted(char_map.items()))

            if key in mappings:
                mappings[key].append(s)
            else:
                mappings[key] = [s]

        
        res = [value for value in mappings.values()]

        return res

            



        