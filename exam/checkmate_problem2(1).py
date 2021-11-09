board = []

for row_index in range(len(board)):
    for column_index in range (len(board[row_index])):
        if board[row_index][column_index] == 'Q':
            pass

queens = []
for row_index in range(len(board)):
    for column_index in range (len(board[row_index])):
        if board[row_index][column_index] == 'Q':
            queens.append((row_index, column_index))

for queen in queens:
    pass