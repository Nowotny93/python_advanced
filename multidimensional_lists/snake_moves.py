def create_blank_matrix(row_size, col_size):
    matrix = []
    for _ in range (row_size):
        matrix.append([])
        for _ in range (col_size):
            matrix[-1].append('')
    return matrix

n, m = input().split()
n, m = int(n), int(m)
text = input()

matrix = create_blank_matrix(n , m)

text_index = 0
col = 0
for row in range(n):

    if row % 2 == 0:
        dir = 1
    else:
        dir = -1
    while 0 <= col < m:
        snake_pos = row, col
        matrix[row][col] = text[text_index]

        if text_index + 1 == len(text):
            text_index = -1
        text_index += 1
        col += dir
    col -= dir

for i in range(len(matrix)):
    print(''.join(matrix[i]))