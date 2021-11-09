import math

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
        if el == 'P':
            player_row, player_col = int(row), int(col)

game_over = False
coins = 0
general_player_path = []
while True:
    command = input()
    player_row, player_col = get_next_position(command, player_row, player_col)
    if is_outside(player_row, player_col, rows):
        game_over = True
        break
    elif matrix[player_row][player_col] == 'X':
        game_over = True
        break
    else:
        player_path = []
        player_path.append(player_row)
        player_path.append(player_col)
        general_player_path.append(player_path)
        coins += int(matrix[player_row][player_col])
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break

if game_over:
    print(f"Game over! You've collected {math.floor(coins / 2)} coins.")
print('Your path:')
for coordinates in general_player_path:
    print(coordinates)