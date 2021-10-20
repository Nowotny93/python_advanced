def is_valid(m_matrix, matrix_row, matrix_col):
    if 0 <= matrix_row < len(m_matrix[0]) and 0 <= matrix_col < len(m_matrix[0]):
        return True
    else:
        print('Invalid coordinates')

def add_function(m_matrix, matrix_row, matrix_col, matrix_value):
    m_matrix[matrix_row][matrix_col] += matrix_value
    return m_matrix

def subtract_function(m_matrix, matrix_row, matrix_col, matrix_value):
    m_matrix[matrix_row][matrix_col] -= matrix_value
    return m_matrix

rows = int(input())

matrix = []
for i in range (rows):
    matrix.append([int(x) for x in input().split()])

command = input()
while command != 'END':
    command_splt = command.split()
    row = int(command_splt[1])
    col = int(command_splt[2])
    value = int(command_splt[3])
    if command_splt[0] == 'Add' and is_valid(matrix, row, col):
        matrix = add_function(matrix, row, col,value)
    elif command_splt[0] == 'Subtract' and is_valid(matrix, row, col):
        matrix = subtract_function(matrix, row, col, value)
    command = input()

for row in matrix:
    print(' '.join([str(x) for x in row]))