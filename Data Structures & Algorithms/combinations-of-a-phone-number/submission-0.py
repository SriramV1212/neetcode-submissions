class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []


        map = {"2":["a","b","c"], "3":["d","e","f"],"4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}

        result = []

        def dfs(i, path):
            if i == len(digits):
                result.append("".join(path.copy()))
                return

            number = digits[i]
            characters = map[number]

            for char in characters:
                path.append(char)
                dfs(i+1,path)
                path.pop()

        dfs(0,[])

        return result











