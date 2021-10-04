number_of_names = int(input())

dictionary_set = set([])

for i in range(1, number_of_names + 1):
    dictionary_set.add(input())

for name in dictionary_set:
    print(name)