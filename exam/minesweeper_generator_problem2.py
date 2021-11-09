def get_next_position(row, col, s, m):
    if col + 1 >= s:
        pass
    else:
        if m[row][col + 1] == '*':
            m[row][col] += 1
    if row + 1 >= s or col + 1 >= s:
        pass
    else:
        if m[row + 1][col + 1] == '*':
            m[row][col] += 1
    if row + 1 >= s:
        pass
    else:
        if m[row + 1][col] == '*':
            m[row][col] += 1
    if row + 1 >= s or col - 1 < 0:
        pass
    else:
        if m[row + 1][col - 1] == '*':
            m[row][col] += 1
    if col - 1 < 0:
        pass
    else:
        if m[row][col - 1] == '*':
            m[row][col] += 1
    if row - 1 < 0 or col - 1 < 0:
        pass
    else:
        if m[row - 1][col - 1] == '*':
            m[row][col] += 1
    if row - 1 < 0:
        pass
    else:
        if m[row - 1][col] == '*':
            m[row][col] += 1
    if row - 1 < 0 or col + 1 >= s:
        pass
    else:
        if m[row - 1][col + 1] == '*':
            m[row][col] += 1

size = int(input())
bombs = int(input())

matrix = []
cells = size * '0'

for row in range(size):
    matrix.append([int(x) for x in cells])

for i in range(bombs):
    coordinates = input()
    bomb_row = int(coordinates[1])
    bomb_col = int(coordinates[-2])
    matrix[bomb_row][bomb_col] = '*'

for player_row in range(size):
    for player_col in range(size):
        current_pos = matrix[player_row][player_col]
        if current_pos == '*':
            continue
        else:
            get_next_position(player_row, player_col, size, matrix)

for el in matrix:
    print(' '.join([str(x) for x in el]))