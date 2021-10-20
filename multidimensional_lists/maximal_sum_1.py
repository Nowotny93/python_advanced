import sys

rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range (rows):
    matrix.append([int(x) for x in input().split()])

max_sum = -sys.maxsize
position = None

for row in range (0, rows - 2):
    for col in range (0, cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)

row, col = position
print(f'Sum = {max_sum}')
print(matrix[row][col], matrix[row][col+1], matrix[row][col+2])
print(matrix[row + 1][col], matrix[row+1][col+1], matrix[row+1][col+2])
print(matrix[row + 2][col], matrix[row+2][col+1], matrix[row+2][col+2])