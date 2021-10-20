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

size = int(input())
commands = input().split()

matrix = []

player_row, player_col = 0, 0
for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        el = row_elements[col]
        if el == 's':
            player_row, player_col = int(row), int(col)

pieces_coal = 0
for command in commands:
    initial_row, initial_col = player_row, player_col
    player_row, player_col = get_next_position(command, player_row, player_col)
    if is_outside(player_row, player_col, size):
        player_row, player_col = initial_row, initial_col
        continue
    cell_value = matrix[player_row][player_col]
    if cell_value == 'c':
        matrix[player_row][player_col] = '*'
        location = (player_row, player_col)
        pieces_coal += 1
    elif cell_value == 'e':
        location = player_row, player_col
        print(f"Game over! {location}")
        exit()
    elif cell_value == '*':
        location = player_row, player_col

coal_count = 0
for sublist in matrix:
    for el in sublist:
        if el == 'c':
            coal_count += 1

if coal_count == 0:
    print(f'You collected all coal! {location}')
else:
    print(f'{coal_count} pieces of coal left. {location}')