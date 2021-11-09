from collections import deque

def best_list_pureness(*args):
    list_of_values = deque(args[0])
    max_pureness = -1
    winning_rotation = 0
    for rotation in range (0, args[-1] + 1):
        pureness = 0
        for idx, el in enumerate((list_of_values)):
            pureness += idx * el
            if pureness > max_pureness:
                max_pureness = pureness
                winning_rotation = rotation
        list_of_values.rotate(1)
    result = f'Best pureness {max_pureness} after {winning_rotation} rotations'
    return result

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)