def is_outside(r, c, rs):
    if r < 0 or c < 0 or r >= rs or c >= rs:
        return True
    return False

def when_hit_is_number(r, c, mx):
    first_num = int(mx[r][0])
    second_cum = int(mx[r][-1])
    third_num = int(mx[0][c])
    fourth_num = int(mx[-1][c])
    return first_num + second_cum + third_num + fourth_num

player_1, player_2 = input().split(', ')
rows = 7

matrix = []

player_row, player_col = 0, 0

for row in range(0, rows):
    row_elements = input().split()
    matrix.append(row_elements)

counter = 0
total_points_player_1 = 501
total_points_player_2 = 501
total_turns_player_1 = 0
total_turns_player_2 = 0
while total_points_player_1 > 0 and total_points_player_2 > 0:
    counter += 1
    cmd = input()
    current_row = int(cmd[1])
    current_col = int(cmd[-2])

    if counter % 2 != 0:
        total_turns_player_1 += 1
        if is_outside(current_row, current_col, rows):
            continue
        if matrix[current_row][current_col].isdigit():
            total_points_player_1 -= int(matrix[current_row][current_col])
        elif matrix[current_row][current_col] == 'D':
            sum_points = when_hit_is_number(current_row, current_col, matrix)
            sum_points_doubled = sum_points * 2
            total_points_player_1 -= sum_points_doubled
        elif matrix[current_row][current_col] == 'T':
            sum_points = when_hit_is_number(current_row, current_col, matrix)
            sum_points_tripled = sum_points * 3
            total_points_player_1 -= sum_points_tripled
        elif matrix[current_row][current_col] == 'B':
            print(f'{player_1} won the game with {total_turns_player_1} throws!')
            exit()
    else:
        total_turns_player_2 += 1
        if is_outside(current_row, current_col, rows):
            continue
        if matrix[current_row][current_col].isdigit():
            total_points_player_2 -= int(matrix[current_row][current_col])
        elif matrix[current_row][current_col] == 'D':
            sum_points = when_hit_is_number(current_row, current_col, matrix)
            sum_points_doubled = sum_points * 2
            total_points_player_2 -= sum_points_doubled
        elif matrix[current_row][current_col] == 'T':
            sum_points = when_hit_is_number(current_row, current_col, matrix)
            sum_points_tripled = sum_points * 3
            total_points_player_2 -= sum_points_tripled
        elif matrix[current_row][current_col] == 'B':
            print(f'{player_2} won the game with {total_turns_player_2} throws!')
            exit()

if total_points_player_1 <= 0:
    print(f'{player_1} won the game with {total_turns_player_1} throws!')
else:
    print(f'{player_2} won the game with {total_turns_player_2} throws!')