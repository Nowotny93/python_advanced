n = int(input())

matrix = []

for row in range (n):
    matrix.append([int(x) for x in input().split(', ')])

l = len(matrix[0])
print (f'Primary diagonal: {", ".join([str(matrix[i][i]) for i in range(l)])}. Sum: {sum([matrix[i][i] for i in range(l)])}')
print (f'Secondary diagonal: {", ".join([str(matrix[l-1-i][i]) for i in range(l-1,-1,-1)])}. Sum: {sum([matrix[l-1-i][i] for i in range(l-1,-1,-1)])}')