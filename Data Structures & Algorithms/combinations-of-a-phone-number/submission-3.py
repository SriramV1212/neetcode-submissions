class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        map = {"2":["a","b","c"], "3":["d","e","f"],"4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}


        res = []

        path = []

        def backtrack(i):
            if len(path) == len(digits):
                res.append("".join(path))
                return

            
            number = digits[i]
            char_map = map[number]

            for char in char_map:
                path.append(char)
                backtrack(i+1)
                path.pop()

        backtrack(0)

        return res



        