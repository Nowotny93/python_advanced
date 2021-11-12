def num_of_player(turn):
    if turn % 2:
        return 1
    return 2

def get_turn(turn, free_r_in_c):
    player = num_of_player(turn)
    while True:
        print(f"Player {player}, please choose a column.")
        number_of_column = input()
        if number_of_column.isnumeric():
            number_of_column = int(number_of_column) - 1
            if number_of_column in range(rows) \
                    and free_r_in_c[number_of_column] >= 0:
                return free_r_in_c[number_of_column], number_of_column, player
        print("Invalid column index!")

def push_mark(i, j, num):
    global game_board
    game_board[i][j] = num

def print_board():
    [print(row) for row in game_board]

def check_for_winner(i, j, num):
    winning_lines = [
        [[[+1, -1], [+2, -2], [+3, -3]], [[-1, +1], [-2, +2], [-3, +3]]],  # diagonal: left,down - right,up
        [[[+1, +1], [+2, +2], [+3, +3]], [[-1, -1], [-2, -2], [-3, -3]]],  # diagonal: right,down - left,up
        [[[0, -1], [0, -2], [0, -3]], [[0, +1], [0, +2], [0, +3]]],  # horizontal: left - right
        [[[+1, 0], [+2, 0], [+3, 0]], [[-1, 0], [-2, 0], [-3, 0]]],  # vertical: down - !(up)
    ]
    for line in winning_lines:
        four_in_line = 1
        for half_line in line:
            for row_col in half_line:
                n_row, n_col = i + row_col[0], j + row_col[1]
                if n_row in range(rows) and n_col in range(columns) and game_board[n_row][n_col] == num:
                    four_in_line += 1
                    if four_in_line == 4:
                        return num
                else:
                    break

rows, columns = [int(x) for x in input().split()]
game_board = [[0 for col in range(columns)] for row in range(rows)]
free_row_in_columns = [rows - 1 for _ in range(columns)]
turns = 1

while True:
    row, col, mark = get_turn(turns, free_row_in_columns)
    free_row_in_columns[col] -= 1
    push_mark(row, col, mark)
    print_board()
    winner = check_for_winner(row, col, mark)
    if winner:
        print(f"The Winner is Player {winner}!")
        break
    if turns == rows * columns:
        print("No winner!")
        break
    turns += 1