# Board is a list of lists, structure like this:
# [[0, 0, 1, 8, 0, 0, 0, 6, 0],
#  [2, 0, 0, 5, 0, 7, 0, 0, 0],
#  [6, 5, 7, 0, 0, 4, 0, 0, 0],
#  [8, 0, 0, 0, 4, 1, 0, 0, 0],
#  [0, 2, 6, 0, 0, 0, 5, 1, 0],
#  [0, 0, 0, 2, 7, 0, 0, 0, 6],
#  [0, 0, 0, 4, 0, 0, 8, 5, 2],
#  [0, 0, 0, 7, 0, 9, 0, 0, 4],
#  [0, 6, 0, 0, 0, 2, 9, 0, 0]]

# Box starting positions
box_pos = [ {0,0}, {0,3}, {0,6}, {3,0}, {3,3}, {3,6}, {6,0}, {6,3}, {6,6} ]


def solve_sudoku(board):
    permanent_board = [False * 9] * 9
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell != 0:
                permanent_board[i][j] = True

    curr_row = 0
    curr_col = 0
    while curr_row < 9:
        while curr_col < 9:
            if not permanent_board[curr_row][curr_col]:
                pass
    pass

def is_valid(board, row, col):
    curr_row = get_row_no_zeroes(board, row)
    curr_col = get_col_no_zeroes(board, col)
    curr_box = get_box_no_zeroes(board, row, col)
    if len(curr_row) != len(set(curr_row)):
        return False
    elif len(curr_col) != len(set(curr_col)):
        return False
    elif len(curr_box) != len(set(curr_box)):
        return False
    else:
        return True


def get_row_no_zeroes(board, row):
    return [cell for cell in board[row] if cell > 0]

def get_col_no_zeroes(board, col):
    return [row[col] for row in board if row[col] > 0]

def get_box_no_zeroes(board, row, col):
    box_num = row/3 * 3 + col/3
    curr_row, curr_col = box_pos[box_num]
    box = []
    for i in range(curr_row, curr_row+3):
        for j in range(curr_col, curr_col+3):
            box.append(board[i][j])
    return box

