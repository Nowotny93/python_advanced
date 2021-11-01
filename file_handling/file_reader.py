file = open('numbers.txt', 'r')

sum_nums = 0
for number in file:
    sum_nums += int(number)

print(sum_nums)