class Solution {
public:

    int count = 0;

    bool isValid(vector<string>& board, int row, int col, int n) {

        // Check column
        int i = row - 1;

        while (i >= 0) {
            if (board[i][col] == 'Q') {
                return false;
            }
            i--;
        }

        // Check upper-left diagonal
        i = row - 1;
        int j = col - 1;

        while (i >= 0 && j >= 0) {
            if (board[i][j] == 'Q') {
                return false;
            }
            i--;
            j--;
        }

        // Check upper-right diagonal
        i = row - 1;
        j = col + 1;

        while (i >= 0 && j < n) {
            if (board[i][j] == 'Q') {
                return false;
            }
            i--;
            j++;
        }

        return true;
    }

    void helper(int n, vector<string>& board, int row) {

        // All queens placed
        if (row == n) {
            count++;
            return;
        }

        // Try every column
        for (int col = 0; col < n; col++) {

            if (isValid(board, row, col, n)) {

                // Choose
                board[row][col] = 'Q';

                // Explore
                helper(n, board, row + 1);

                // Backtrack
                board[row][col] = '.';
            }
        }
    }

    int totalNQueens(int n) {

        vector<string> board(n, string(n, '.'));

        helper(n, board, 0);

        return count;
    }
};