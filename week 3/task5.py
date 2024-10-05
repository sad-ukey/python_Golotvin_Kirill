def is_valid_sudoku(board):

    for row in board:
        if not is_valid_row(row):
            return False
    for i in range(9):
        column = [board[j][i] for j in range(9)]
        if not is_valid_row(column):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_row(sub_box):
                return False
    return True


def is_valid_row(row):

    numbers = [x for x in row if x != "."]
    return len(numbers) == len(set(numbers))


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(is_valid_sudoku(board))