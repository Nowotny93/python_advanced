first_nums = set([int(x) for x in input().split()])
second_nums = set([int(z) for z in input().split()])
lines = int(input())

for i in range (1, lines + 1):
    command = input().split()
    if command[0] == 'Add' and command[1] == 'First':
        for el in command:
            if el.isnumeric():
                first_nums.add(int(el))
    elif command[0] == 'Add' and command[1] == 'Second':
        for el in command:
            if el.isnumeric():
                second_nums.add(int(el))
    elif command[0] == 'Remove' and command[1] == 'First':
        for el in command:
            if el.isnumeric() and int(el) in first_nums:
                first_nums.remove(int(el))
    elif command[0] == 'Remove' and command[1] == 'Second':
        for el in command:
            if el.isnumeric() and int(el) in second_nums:
                second_nums.remove(int(el))
    elif command[0] == 'Check':
        if first_nums < second_nums:
            print('True')
        elif second_nums < first_nums:
            print('True')
        else:
            print('False')

first_nums_sorted = sorted(first_nums)
second_nums_sorted = sorted(second_nums)
first_nums_as_str = [str(x) for x in first_nums_sorted]
second_nums_as_str = [str(z) for z in second_nums_sorted]
print(', '.join(first_nums_as_str))
print(', '.join(second_nums_as_str))