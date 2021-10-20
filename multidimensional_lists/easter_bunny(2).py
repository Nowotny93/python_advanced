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

player_row = 0
player_col = 0

for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(rows):
        el = row_elements[col]
        if el == 'B':
            player_row, player_col = int(row), int(col)

directions = {
    "up": {"coordinates": [], "points" : 0},
    "down": {"coordinates": [], "points" : 0},
    "left": {"coordinates": [], "points" : 0},
    "right": {"coordinates": [], "points" : 0},
}

init_pr = player_row
init_pc = player_col
counter = 0
points = 0
right_direction = 0
right_path = 0
max_points = 0
while counter < len(directions):
    for direction in directions:
        counter += 1
        player_row, player_col = init_pr, init_pc
        player_row, player_col = get_next_position(direction, player_row, player_col)
        while not is_outside(player_row, player_col, rows) and matrix[player_row][player_col] != 'X':
            points += int(matrix[player_row][player_col])
            coordinates = [player_row, player_col]
            directions[direction]['coordinates'].append(coordinates)
            directions[direction]['points'] += int(matrix[player_row][player_col])
            player_row, player_col = get_next_position(direction, player_row, player_col)
        if points > max_points:
            max_points = directions[direction]['points']
            right_path = directions[direction]['coordinates']
            right_direction = direction
        points = 0

print(right_direction)

for el in right_path:
    print(el)

print(max_points)