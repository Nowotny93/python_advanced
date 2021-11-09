def is_valid(row, col, n):
    return 0 <= row < n and 0 <= col <= row

def get_magic_triangle(n, triangle=[[1], [1, 1]]):
    for rows in range(2, n):
        row = []
        for col in range(rows + 1):
            num_1, num_2 = 0, 0
            if is_valid(rows - 1, col - 1, n):
                num_1 = triangle[rows - 1][col - 1]
            if is_valid(rows - 1, col, n):
                num_2 = triangle[rows - 1][col]
            row.append(num_1 + num_2)
        triangle.append(row)
    return triangle

print(get_magic_triangle(5))