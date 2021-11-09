def best_list_pureness(*args):
    list_of_values = args[0]
    max_pureness = -1
    winning_rotation = 0
    for rotation in range (0, args[-1] + 1):
        pureness = 0
        for idx in range(0, len(list_of_values)):
            pureness += idx * list_of_values[idx]
            if pureness > max_pureness:
                max_pureness = pureness
                winning_rotation = rotation
        rotated_value = list_of_values.pop()
        list_of_values.insert(0, rotated_value)
    result = f'Best pureness {max_pureness} after {winning_rotation} rotations'
    return result

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)