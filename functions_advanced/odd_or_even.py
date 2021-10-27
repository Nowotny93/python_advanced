def function_odd(odd_nums, all_nums):
    print(sum(odd_nums) * len(all_nums))

def function_even(even_nums, all_nums):
    print(sum(even_nums) * len(all_nums))

command = input()
numbers = [int(x) for x in input().split()]

if command == 'Even':
    even_numbers = [x for x in numbers if x % 2 == 0]
    function_even(even_numbers, numbers)
else:
    odd_numbers = [x for x in numbers if x % 2 != 0]
    function_odd(odd_numbers, numbers)