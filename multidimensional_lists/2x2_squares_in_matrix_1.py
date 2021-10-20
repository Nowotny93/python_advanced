rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range (rows):
    matrix.append([x for x in input().split()])

identical_total = 0

for row in range (rows - 1, 0, -1):
    for col in range (cols - 1, 0, -1):
        if matrix[row][col] == matrix[row][col - 1] == matrix[row - 1][col] == matrix[row - 1][col - 1]:
            identical_total += 1

print(identical_total)