rows = int(input())

matrix = []

player_row = 0
player_col = 0

traps = []
for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(rows):
        el = row_elements[col]
        if el == 'B':
            player_row, player_col = int(row), int(col)
        elif el == 'X':
            traps.append([row, col])

sum_right = 0
dict_right = {'right': []}
for right in range (player_col + 1, rows):
    el = matrix[player_row][right]
    if el != 'X':
        sum_right += int(el)
        location = [player_row, right]
        dict_right['right'].append(location)
    else:
        break

sum_up = 0
dict_up = {'up': []}
for up in range (1, player_row + 1):
    el = matrix[player_row - up][player_col]
    if el != 'X':
        sum_up += int(el)
        location = [player_row - up, player_col]
        dict_up['up'].append(location)
    else:
        break

sum_left = 0
dict_left = {'left': []}
for left in range (player_col - 1, 0, -1):
    el = matrix[player_row][left]
    if el != 'X':
        sum_left += int(el)
        location = [player_row, left]
        dict_left['left'].append(location)
    else:
        break

sum_down = 0
dict_down = {'down': []}
for down in range (player_row + 1, rows):
    el = matrix[down][player_col]
    if el != 'X':
        sum_down += int(el)
        location = [down, player_col]
        dict_down['down'].append(location)
    else:
        break

if sum_right > sum_up and sum_right > sum_down and sum_right > sum_left:
    print('right')
    for value in dict_right.values():
        for el in value:
            print(el)
    print(sum_right)

elif sum_up > sum_down and sum_up > sum_right and sum_up > sum_left:
    print('up')
    for value in dict_up.values():
        for el in value:
            print(el)
    print(sum_up)

elif sum_left > sum_down and sum_left > sum_right and sum_left > sum_up:
    print('left')
    for value in dict_left.values():
        for el in value:
            print(el)
    print(sum_left)

elif sum_down > sum_left and sum_down > sum_right and sum_down > sum_up:
    print('down')
    for value in dict_down.values():
        for el in value:
            print(el)
    print(sum_down)