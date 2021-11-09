from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

dictionary = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    result = material + magic

    if 100 <= result <= 199:
        dictionary['Gemstone'] += 1
    elif 200 <= result <= 299:
        dictionary['Porcelain Sculpture'] += 1
    elif 300 <= result <= 399:
        dictionary['Gold'] += 1
    elif 400 <= result <= 499:
        dictionary['Diamond Jewellery'] += 1
    elif result < 100:
        if result % 2 == 0:
            doubled_material = material * 2
            tripled_magic = magic * 3
            new_result = doubled_material + tripled_magic
            if 100 <= new_result <= 199:
                dictionary['Gemstone'] += 1
            elif 200 <= new_result <= 299:
                dictionary['Porcelain Sculpture'] += 1
            elif 300 <= new_result <= 399:
                dictionary['Gold'] += 1
            elif 400 <= new_result <= 499:
                dictionary['Diamond Jewellery'] += 1
        elif result % 2 != 0:
            doubled_result = result * 2
            if 100 <= doubled_result <= 199:
                dictionary['Gemstone'] += 1
            elif 200 <= doubled_result <= 299:
                dictionary['Porcelain Sculpture'] += 1
            elif 300 <= doubled_result <= 399:
                dictionary['Gold'] += 1
            elif 400 <= doubled_result <= 499:
                dictionary['Diamond Jewellery'] += 1
    elif result > 499:
        divided_result = result / 2
        if 100 <= divided_result <= 199:
            dictionary['Gemstone'] += 1
        elif 200 <= divided_result <= 299:
            dictionary['Porcelain Sculpture'] += 1
        elif 300 <= divided_result <= 399:
            dictionary['Gold'] += 1
        elif 400 <= divided_result <= 499:
            dictionary['Diamond Jewellery'] += 1

if (dictionary['Gemstone'] != 0 and dictionary['Porcelain Sculpture'] != 0) or (dictionary['Gold'] != 0 and dictionary['Diamond Jewellery'] != 0):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if len(materials) != 0:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
elif len(magic_level) != 0:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')

for key, value in sorted(dictionary.items()):
    if value != 0:
        print(f'{key}: {value}')