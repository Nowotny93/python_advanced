def is_outside(r, c, rows):
    if r < 0 or c < 0 or r >= rows or c >= rows:
        return True
    return False

matrix = []
rows = 6

for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)

sum_points = 0
trow = 0
while trow < 3:
    trow += 1
    coorindates = input()[1:-1].split(', ')
    player_row = int(coorindates[0])
    player_col = int(coorindates[1])
    if is_outside(player_row, player_col, rows) or matrix[player_row][player_col] != 'B':
        continue
    else:
        if matrix[player_row][player_col] == 'B':
            for idx_down in range (player_row + 1, 6):
                sum_points += int(matrix[idx_down][player_col])

            for idx_up in range (player_row - 1, -1, -1):
                sum_points += int(matrix[idx_up][player_col])

            matrix[player_row][player_col] = 0

if 100 <= sum_points <= 199:
    print(f"Good job! You scored {sum_points} points, and you've won Football.")
elif 200 <= sum_points <= 299:
    print(f"Good job! You scored {sum_points} points, and you've won Teddy Bear.")
elif sum_points >= 300:
    print(f"Good job! You scored {sum_points} points, and you've won Lego Construction Set.")
else:
    needed_points = 100 - sum_points
    print(f'Sorry! You need {needed_points} points more to win a prize.')