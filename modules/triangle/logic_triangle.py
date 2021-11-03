def triangle_size_first(size):
    for row in range (1, size+1):
        for col in range(1, row + 1):
            print(col, end= " ")
        print()

def triangle_size_second(size):
    for row in range(size, 1, -1):
        for col in range(1, row):
            print(col, end =" ")
        print()

def print_triangle(size):
    triangle_size_first(size)
    triangle_size_second(size)

