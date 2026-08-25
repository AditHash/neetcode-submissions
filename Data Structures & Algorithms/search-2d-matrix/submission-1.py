class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        row = 0
        col = m-1

        while (col >= 0 and row < n):
            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] > target):
                col = col - 1 
            else:
                row = row + 1
        return False
        