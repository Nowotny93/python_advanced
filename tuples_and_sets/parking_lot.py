number_of_commands = int(input())

car_numbers_set = set([])

for i in range(1, number_of_commands + 1):
    command_number = input().split(', ')
    command, number = command_number
    if command == 'IN':
        car_numbers_set.add(number)
    else:
        car_numbers_set.remove(number)

if not car_numbers_set:
    print('Parking Lot is Empty')
else:
    for car in car_numbers_set:
        print(car)