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
for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(rows):
        el = row_elements[col]
        if el == 'A':
            player_row, player_col = int(row), int(col)

tea_bags = 0
matrix[player_row][player_col] = '*'
while True:
    command = input()
    player_row, player_col = get_next_position(command, player_row, player_col)
    if is_outside(player_row, player_col, rows):
        break
    cell_value = matrix[player_row][player_col]
    matrix[player_row][player_col] = '*'
    if cell_value == 'R':
        break
    if cell_value.isdigit():
        tea_bags += int(cell_value)
        if tea_bags >= 10:
            break

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print('She did it! She went to the party.')

for el in matrix:
    print(' '.join(el))