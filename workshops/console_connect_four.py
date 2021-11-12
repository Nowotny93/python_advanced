DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7
DEFAULT_WIN_CONDITION_COUNT = 4

def get_player_choice_func(is_test=False):
    def get_player_choice(player):
        print(f'Player {player}, please choose a column')
        return int(input()) - 1
    choices_for_test = [1, 2, 2, 3, 3, 4, 1, 5]
    choices_for_test = [1, 2, 1, 2, 1, 2, 1]
    choices_for_test = [1, 2, 2, 4, 3, 3, 3, 7, 4, 4, 4]
    choices_for_test = [4, 3, 3, 1, 2, 2, 2, 7, 1, 1, 1]
    choices_for_test_index = 0
    def get_player_choice_for_test(player):
        nonlocal choices_for_test_index
        print(f'Player {player}, please choose a column')
        choice = choices_for_test[choices_for_test_index]
        print(choice)
        choices_for_test_index += 1
        return choice - 1
    if is_test:
        return get_player_choice_for_test
    else:
        return get_player_choice

def get_lowest_free_row_index(board, column_index):
    rows_count = len(board)
    for row_index in range (rows_count - 1, -1, -1):
        if board[row_index][column_index] == 0:
            return row_index
    return None

def apply_player_choice(board, column_index, player):
    row_index = get_lowest_free_row_index(board, column_index)
    board[row_index][column_index] = player
    return board

def in_range(value, max_value):
    return 0 <= value < max_value

def is_win_condition_value(board, row_index, column_index, player, rows_count, columns_count):
    return in_range(column_index, columns_count) \
           and in_range(row_index, rows_count) \
           and board[row_index][column_index] == player

def has_win_condition_from_position(board, row_index, column_index, player, win_condition_count=DEFAULT_WIN_CONDITION_COUNT):
    rows_count = len(board)
    columns_count = len(board[0])
    horizontal_values = [is_win_condition_value(board, row_index, column_index + d, player, rows_count, columns_count)
                         for d in range(win_condition_count)]
    vertical_values = [is_win_condition_value(board, row_index + d, column_index, player, rows_count, columns_count)
                       for d in range(win_condition_count)]
    left_diagonal_values = [is_win_condition_value(board, row_index + d, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]
    right_diagonal_values = [is_win_condition_value(board, row_index + d, column_index + d, player, rows_count, columns_count)
                            for d in range(win_condition_count)]
    return all(horizontal_values) or all(vertical_values) or all(left_diagonal_values) or all(right_diagonal_values)

def has_win_condition(board, player):
    rows_count = len(board)
    for row_index in range (rows_count):
        columns_count = len(board[row_index])
        for column_index in range (columns_count):
            if has_win_condition_from_position(board, row_index, column_index, player):
                return True
    return False

def print_board(board):
    for row in board:
        print(row)

def print_winner_message(player):
    print(f'The winner is {player}')

def play(board, player=1):
    while True:
        player_choice = get_player_choice(player)
        apply_player_choice(board, player_choice, player)
        print_board(board)
        if has_win_condition(board, player):
            print_winner_message(player)
            break
        player = 2 if player == 1 else 1
    #else:
        #play(board, player=2)

def create_board(rows_count = DEFAULT_ROWS_COUNT, columns_count = DEFAULT_COLUMNS_COUNT):
    return [[0] * columns_count for _ in range (rows_count)]

get_player_choice = get_player_choice_func(is_test=False)
board = create_board()
play(board)