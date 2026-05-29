class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols, = len(matrix), len(matrix[0])
        x_index, y_index = [], []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    x_index.append(i)
                    y_index.append(j)
        for i in range(rows):
            for j in range(cols):
                if i in x_index or j in y_index:
                    matrix[i][j] = 0
        
        
