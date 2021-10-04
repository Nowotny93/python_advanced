number_of_intersections = int(input())

first_set = set([])
second_set = set([])
max_len = 0
longest_set = 0

for i in range (1, number_of_intersections + 1):
    random_intersection = input().split('-')
    first_inter_list = random_intersection[0].split(',')
    second_inter_list = random_intersection[1].split(',')

    for z in range (int(first_inter_list[0]), int(first_inter_list[1]) + 1):
        first_set.add(z)

    for y in range (int(second_inter_list[0]), int(second_inter_list[1]) + 1):
        second_set.add(y)

    intersected_set = first_set & second_set
    if len(intersected_set) > max_len:
        max_len = len(intersected_set)
        longest_set = intersected_set
    first_set.clear()
    second_set.clear()

longest_set_list = [str(x) for x in longest_set]
print(f'Longest intersection is [{", ".join(longest_set_list)}] with length {max_len}')