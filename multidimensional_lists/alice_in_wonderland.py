def is_inside(rows, r, c):
    return 0 <= r < rows and 0 <= c < rows

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

traps = []
for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(rows):
        el = row_elements[col]
        if el == 'A':
            player_row, player_col = int(row), int(col)
        elif el == 'R':
            traps.append([row, col])

commands = input()

is_fail = False
bags_of_tea = 0
while is_fail == False and bags_of_tea < 10:
    next_player_row, next_player_col = get_next_position(commands, player_row, player_col)
    if not is_inside(rows, next_player_row, next_player_col):
        is_fail = True
        break
    if commands == 'down':
        for down in range (player_row + 1, rows):
            el = matrix[down][player_col]
            if el == '.' or el == '*':
                matrix[player_row][player_col] = '*'
                matrix[down][player_col] = '*'
                player_row = down
                break
            elif el.isnumeric():
                bags_of_tea += int(el)
                matrix[player_row][player_col] = '*'
                matrix[down][player_col] = '*'
                player_row = down
                break
            elif el == 'R':
                is_fail = True
                matrix[player_row][player_col] = '*'
                matrix[down][player_col] = '*'
                break
    elif commands == 'right':
        for right in range(player_col + 1, rows):
            el = matrix[player_row][right]
            if el == '.' or el == '*':
                matrix[player_row][player_col] = '*'
                matrix[player_row][right] = '*'
                player_col = right
                break
            elif el.isnumeric():
                bags_of_tea += int(el)
                matrix[player_row][player_col] = '*'
                matrix[player_row][right] = '*'
                player_col = right
                break
            elif el == 'R':
                is_fail = True
                player_col = right
                matrix[player_row][player_col] = '*'
                matrix[player_row][right] = '*'
                break
    elif commands == 'left':
        for left in range(player_col - 1, -1, -1):
            el = matrix[player_row][left]
            if el == '.' or el == '*':
                matrix[player_row][player_col] = '*'
                matrix[player_row][left] = '*'
                player_col = left
                break
            elif el.isnumeric():
                bags_of_tea += int(el)
                matrix[player_row][player_col] = '*'
                matrix[player_row][left] = '*'
                player_col = left
                break
            elif el == 'R':
                is_fail = True
                player_col = left
                matrix[player_row][player_col] = '*'
                matrix[player_row][left] = '*'
                break
    elif commands == 'up':
        for up in range(1, player_row + 1):
            el = matrix[player_row - up][player_col]
            if el == '.' or el == '*':
                matrix[player_row][player_col] = '*'
                matrix[player_row - up][player_col] = '*'
                player_row = up
                break
            elif el.isnumeric():
                bags_of_tea += int(el)
                matrix[player_row][player_col] = '*'
                matrix[player_row - up][player_col] = '*'
                player_row = up
                break
            elif el == 'R':
                is_fail = True
                player_row = up
                matrix[player_row][player_col] = '*'
                matrix[player_row - up][player_col] = '*'
                break
    if is_fail == True or bags_of_tea >= 10:
        break
    else:
        commands = input()

if is_fail:
    print("Alice didn't make it to the tea party.")
else:
    print('She did it! She went to the party.')

for el in matrix:
    print(' '.join(el))