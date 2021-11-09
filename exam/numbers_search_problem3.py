import collections

def numbers_searching(*args):
    output = []
    unique_nums = sorted([item for item, count in collections.Counter(args).items() if count > 1])
    max_num = max(args)
    min_num = min(args)
    for i in range (min_num, max_num + 1):
        if i not in args:
            missing_value = i
            output.append(i)
            break
    output.append(unique_nums)
    return output

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))