size = int(input())

matrix = []

for row in range(size):
    row_elements = [int(x) for x in input().split()]
    matrix.append(row_elements)

for location in input().split():
    bomb_row, bomb_col = int(location[0]), int(location[2])
    bomb = matrix[bomb_row][bomb_col]
    if bomb == 0:
        continue
    matrix[bomb_row][bomb_col] = 0
    if 0 <= bomb_row + 1 < size and 0 <= bomb_col < size and matrix[bomb_row + 1][bomb_col] > 0:
        matrix[bomb_row + 1][bomb_col] -= bomb
    if 0 <= bomb_row + 1 < size and 0 <= bomb_col - 1 < size and matrix[bomb_row + 1][bomb_col -1] > 0:
        matrix[bomb_row + 1][bomb_col -1] -= bomb
    if 0 <= bomb_row < size and 0 <= bomb_col - 1 < size and matrix[bomb_row][bomb_col - 1] > 0:
        matrix[bomb_row][bomb_col - 1] -= bomb
    if 0 <= bomb_row - 1 < size and 0 <= bomb_col - 1 < size and matrix[bomb_row - 1][bomb_col - 1] > 0:
        matrix[bomb_row - 1][bomb_col - 1] -= bomb
    if 0 <= bomb_row - 1 < size and 0 <= bomb_col < size and matrix[bomb_row - 1][bomb_col] > 0:
        matrix[bomb_row - 1][bomb_col] -= bomb
    if 0 <= bomb_row - 1 < size and 0 <= bomb_col + 1 < size and matrix[bomb_row - 1][bomb_col + 1] > 0:
        matrix[bomb_row - 1][bomb_col + 1] -= bomb
    if 0 <= bomb_row < size and 0 <= bomb_col + 1 < size and matrix[bomb_row][bomb_col + 1] > 0:
        matrix[bomb_row][bomb_col + 1] -= bomb
    if 0 <= bomb_row + 1 < size and 0 <= bomb_col + 1 < size and matrix[bomb_row + 1][bomb_col + 1] > 0:
        matrix[bomb_row + 1][bomb_col + 1] -= bomb

count_active_sells = 0
sum = 0
for el in matrix:
    for sub_el in el:
        if sub_el > 0:
            count_active_sells += 1
            sum += sub_el

print (f'Alive cells: {count_active_sells}')
print(f'Sum: {sum}')

for sublist in matrix:
    sublist = [str(x) for x in sublist]
    print(' '.join(sublist))