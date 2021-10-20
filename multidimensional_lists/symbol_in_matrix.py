rows = int(input())

matrix = []

for row in range(rows):
    el = ','.join(input())
    lines = [ord(x) for x in el.split(",")]
    matrix.append(lines)

symbol = input()

for row in range (rows):
    for column in range (rows):
        if matrix[row][column] == ord(symbol):
            location = [row, column]
            print(f"({location[0]}, {location[1]})")
            exit()

print(f'{symbol} does not occur in the matrix')