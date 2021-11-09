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

rows = int(input())

matrix = []

player_row, player_col = 0, 0
hole_1_row, hole_1_col = 0, 0
hole_2_row, hole_2_col = 0, 0

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(rows):
        el = row_elements[col]
        if el == 'S':
            player_row, player_col = int(row), int(col)
        if el == 'B':
            if hole_1_row != 0 and hole_1_col != 0:
                hole_1_row, hole_1_col = int(row), int(col)
            else:
                hole_2_row, hole_2_col = int(row), int(col)

food_counter = 0
matrix[player_row][player_col] = 'S'
while True:
    matrix[player_row][player_col] = '.'
    command = input()
    player_row, player_col = get_next_position(command, player_row, player_col)
    if is_outside(player_row, player_col, rows):
        print('Game over!')
        print(f'Food eaten: {food_counter}')
        break
    if matrix[player_row][player_col] == 'B':
        matrix[player_row][player_col] = '.'
        matrix[hole_2_row][hole_2_col] = 'S'
        player_row, player_col = hole_2_row, hole_2_col
        continue
    if matrix[player_row][player_col] == '*':
        food_counter += 1
    matrix[player_row][player_col] = 'S'
    if food_counter == 10:
        print('You won! You fed the snake.')
        print(f'Food eaten: {food_counter}')
        break

for submatrix in matrix:
    print(f"{''.join(submatrix)}")