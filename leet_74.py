def searchMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while ((row < len(matrix)) & (col >= 0)):
        if matrix[row][col] == target:
            return True
        elif matrix[row][col]< target:
            row+= 1
        else:
            col -= 1
    return False 
