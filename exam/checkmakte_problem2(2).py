def read_board(is_test = False):
    if is_test:
        return [
            ['.','.','.','.','.','.','.','.'],
            ['Q','.','.','.','.','.','.','.'],
            ['.','K','.','.','.','Q','.','.'],
            ['.','.','.','Q','.','.','.','.'],
            ['Q','.','.','.','Q','.','.','.'],
            ['.','Q','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','Q','.'],
            ['.','Q','.','Q','.','.','.','.'],
        ]
    return [input().split() for _ in range(8)]

def find_king_position(board):
    for row_index in range(len(board)):
        if 'K' in board[row_index]:
            column_index = board[row_index].index('K')
            return (row_index, column_index)

def is_in_range(value, max_value):
    return 0 <= value < max_value

def search_with_deltas(board, king, deltas):
    rows_count = len(board)
    columns_count = len(board[0])
    (row_index, column_index) = king
    (delta_row, delta_column) = deltas
    while True:
        if not is_in_range(row_index, rows_count) or not is_in_range(column_index, columns_count):
            return None
        if board[row_index][column_index] == 'Q':
            return [row_index, column_index]
        row_index += delta_row
        column_index += delta_column

def get_capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
    ]
    queens = [
        search_with_deltas(board, king, delta)
        for delta in deltas
    ]
    return [queen for queen in queens if queen]

def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print('The king is safe!')

board = read_board()
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)