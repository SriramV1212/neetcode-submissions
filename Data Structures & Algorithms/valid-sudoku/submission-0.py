class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] in seen:
                    return False
                elif board[r][c] != ".":
                    seen.add(board[r][c])

        
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] in seen:
                    return False
                elif board[r][c] != ".":
                    seen.add(board[r][c])


        row, col = 0, 0

        while row < 9:
            while col < 9:

                seen = set()

                for r in range(row,row+3):
                    for c in range(col,col+3):
                        if board[r][c] in seen:
                            return False
                        elif board[r][c]!=".":
                            seen.add(board[r][c])

                col+=3

            row+=3

        return True

 




        