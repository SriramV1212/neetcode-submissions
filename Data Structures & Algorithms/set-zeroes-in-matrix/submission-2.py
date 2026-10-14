class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        zero_row = set()
        zero_column = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if r not in zero_row:
                        zero_row.add(r)
                    if c not in zero_column:
                        zero_column.add(c)
        

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0 and (r in zero_row and c in zero_column):
                    i = 0
                    j = 0

                    while i < len(matrix[0]):
                        matrix[r][i] = 0
                        i+=1

                    while j < len(matrix):
                        matrix[j][c] = 0
                        j+=1

        return None


        
        