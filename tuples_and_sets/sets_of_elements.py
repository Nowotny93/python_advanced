both_sets = input().split()
numbers_first_set = int(both_sets[0])
numbers_second_set = int(both_sets[1])

first_set = set([])
second_set = set([])

for num in range (1, numbers_first_set + 1):
    first_set.add(int(input()))

for num_2 in range(1, numbers_second_set + 1):
    second_set.add(int(input()))

unique_numbers = first_set & second_set
for number in unique_numbers:
    print(number)