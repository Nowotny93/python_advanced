rows = int(input())

matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(lines)

print(matrix)