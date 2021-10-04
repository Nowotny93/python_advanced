number_of_names = int(input())

even_set = set([])
odd_set = set([])
sum_of_ascii_values_per_name = 0

for i in range (1, number_of_names + 1):
    name = input()
    for ch in name:
        ascii_value = ord(ch)
        sum_of_ascii_values_per_name += ascii_value

    needed_ascii_value = int(sum_of_ascii_values_per_name / i)
    if needed_ascii_value % 2 == 0:
        even_set.add(needed_ascii_value)
    else:
        odd_set.add(needed_ascii_value)
    sum_of_ascii_values_per_name = 0

sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)

if sum_odd_set == sum_even_set:
    union_of_sets = odd_set | even_set
    union_of_sets_list = [str(x) for x in union_of_sets]
    print(", ".join(union_of_sets_list))
elif sum_odd_set > sum_even_set:
    difference_of_sets = odd_set - even_set
    difference_of_sets_list = [str(x) for x in difference_of_sets]
    print(", ".join(difference_of_sets_list))
elif sum_odd_set < sum_even_set:
    symmetric_difference_of_sets = odd_set ^ even_set
    symmetric_difference_of_sets_list = [str(x) for x in symmetric_difference_of_sets]
    print(", ".join(symmetric_difference_of_sets_list))