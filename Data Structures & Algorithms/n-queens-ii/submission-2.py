class Solution:
    def totalNQueens(self, n: int) -> int:

        count = 0
        board = [["."] * n for b in range(n)]

        def isValid(board, row, col, n):

            # Check column
            i = row - 1

            while i >= 0:
                if board[i][col] == "Q":
                    return False
                i -= 1

            # Check upper-left diagonal
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def helper(board, row):

            nonlocal count

            # All queens placed
            if row == n:
                count += 1
                return

            # Try every column in this row
            for col in range(n):

                if isValid(board, row, col, n):

                    # Choose
                    board[row][col] = "Q"

                    # Explore
                    helper(board, row + 1)

                    # Backtrack
                    board[row][col] = "."

        helper(board, 0)

        return count