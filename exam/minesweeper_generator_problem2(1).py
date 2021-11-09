def get_next_position(row, col, s, m):
    try:
        if m[row][col + 1] == '*' and col + 1 < s:
            m[row][col] += 1
    except IndexError:
        pass
    try:
        if m[row + 1][col + 1] == '*' and col + 1 < s and row + 1 < s:
            m[row][col] += 1
    except IndexError:
        pass
    try:
        if m[row + 1][col] == '*' and row + 1 < s:
            m[row][col] += 1
    except IndexError:
        pass
    try:
        if m[row + 1][col - 1] == '*' and row + 1 < s and col - 1 >= 0:
            m[row][col] += 1
    except IndexError:
        pass
    if m[row][col - 1] == '*' and col - 1 >= 0:
        m[row][col] += 1
    if m[row - 1][col - 1] == '*' and col - 1 >= 0 and row - 1 >= 0:
        m[row][col] += 1
    if m[row - 1][col] == '*' and row - 1 >= 0:
        m[row][col] += 1
    try:
        if m[row - 1][col + 1] == '*' and row - 1 >= 0 and col + 1 < s:
            m[row][col] += 1
    except IndexError:
        pass
    return m[row][col]

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