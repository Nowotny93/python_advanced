def is_outside(r, c, rows):
    if r < 0 or c < 0 or r >= rows or c >= rows:
        return True
    return False

def get_next_position(direction, row, col):
    if direction == 'up':
        return (row - 1, col)
    if direction == 'down':
        return (row + 1, col)
    if direction == 'left':
        return (row, col - 1)
    return (row, col + 1)

initial_str = list(input())
rows = int(input())
matrix = []

player_row, player_col = 0, 0
for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(rows):
        el = row_elements[col]
        if el == 'P':
            player_row, player_col = int(row), int(col)

num_cmd = int(input())
for i in range(num_cmd):
    initial_row, initial_col = player_row, player_col
    matrix[player_row][player_col] = '-'
    command = input()
    player_row, player_col = get_next_position(command, player_row, player_col)
    if is_outside(player_row, player_col, rows):
        if len(initial_str) > 0:
            initial_str.pop()
            matrix[initial_row][initial_col] = 'P'
            continue
        else:
            matrix[initial_row][initial_col] = 'P'
            continue
    if (matrix[player_row][player_col]).isalpha():
        initial_str.append(matrix[player_row][player_col])
        matrix[player_row][player_col] = 'P'
    else:
        matrix[player_row][player_col] = 'P'


print(f"{''.join(initial_str)}")
for submatrix in matrix:
    print(f"{''.join(submatrix)}")