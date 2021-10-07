numbers_dictionary = {}

line = input()
while line != "Search":
    try:
        line_int = int(input())
        numbers_dictionary[line] = line_int
    except ValueError:
        print("The variable number must be an integer")
    line = input()

searched_num = input()
while searched_num != "Remove":
    try:
        print(numbers_dictionary[searched_num])
    except ValueError:
        print("Number does not exist in dictionary")
    searched_num = input()

removed_num = input()
while removed_num != 'End':
    try:
        numbers_dictionary.pop(removed_num)
    except KeyError:
        print("Number does not exist in dictionary")
    removed_num = input()

print(numbers_dictionary)