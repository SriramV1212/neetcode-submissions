class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, path, current_word):
            if current_word == word:
                return True

            if not word.startswith(current_word):
                return False
           
            if (r,c) in path:
                return False

            if not 0 <= r < len(board):
                return False
            
            if not 0 <= c < len(board[r]):
                return False

            path.append((r,c))

            if dfs(r-1,c,path,current_word + board[r][c]):
                return True
            if dfs(r+1,c,path,current_word + board[r][c]):
                return True
            if dfs(r,c+1,path,current_word + board[r][c]):
                return True
            if dfs(r,c-1,path,current_word + board[r][c]):
                return True

            path.pop()

            return False

        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if dfs(r,c,[],""):
                    return True

        return False



            




        



            


            

        