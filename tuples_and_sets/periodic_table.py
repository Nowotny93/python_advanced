number_of_lines = int(input())

unique_chemicals = set ([])

for i in range (1, number_of_lines + 1):
    chemicals = input().split()
    for el in chemicals:
        if el not in unique_chemicals:
            unique_chemicals.add(el)

for un_el in unique_chemicals:
    print(un_el)