rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range (rows):
    matrix.append([x for x in input().split()])

command = input()

while command != 'END':
    splt_command = command.split()
    if splt_command[0] == 'swap' and len(splt_command) == 5:
        row_1 = int(splt_command[1])
        col_1 = int(splt_command[2])
        row_2 = int(splt_command[3])
        col_2 = int(splt_command[4])
        if (row_1 < rows and row_1 >= 0 and row_2 < rows and row_2 >= 0) and (col_1 < cols and col_1 >=0 and col_2 < cols and col_2 >= 0):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for i in range (rows):
                print(' '.join(matrix[i]))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()