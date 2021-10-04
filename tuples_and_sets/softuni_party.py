number_of_guests = int(input())

guests = set([])

for i in range (1, number_of_guests + 1):
    reservation_code = input()
    if reservation_code not in guests:
        guests.add(reservation_code)

command = input()

while command != 'END':
    if command in guests:
        guests.remove(command)
    command = input()

guests_list = list(guests)
sorted_list = sorted(guests_list)
print(len(sorted_list))
for code in sorted_list:
    print(code)