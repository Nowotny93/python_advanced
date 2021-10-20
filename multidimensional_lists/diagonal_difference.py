n = int(input())

matrix = []

for row in range (n):
    matrix.append([int(x) for x in input().split()])

abs_difference_diagonals = abs(sum([matrix[i][i] for i in range(n)]) - sum([matrix[n-1-i][i] for i in range(n-1,-1,-1)]))
print(abs_difference_diagonals)