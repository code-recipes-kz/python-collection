class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        # find an empty cell
        row, col = self.find_empty_cell(board)

        # if all cells are filled, return True
        if row == -1 and col == -1:
            return True

        # try digits 1 to 9
        for digit in range(1, 10):
            if self.is_valid(board, row, col, str(digit)):
                # if digit is valid, fill the cell
                board[row][col] = str(digit)

                # recursively solve the remaining board
                if self.solve(board):
                    return True

                # if the remaining board cannot be solved, backtrack and try a different digit
                board[row][col] = '.'

        # if no digit is valid, backtrack to the previous cell
        return False

    def find_empty_cell(self, board):
        # find the first empty cell in the board
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    return row, col
        return -1, -1

    def is_valid(self, board, row, col, digit):
        # check row
        for i in range(9):
            if board[row][i] == digit:
                return False

        # check column
        for j in range(9):
            if board[j][col] == digit:
                return False

        # check sub-box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == digit:
                    return False

        # digit is valid
        return True