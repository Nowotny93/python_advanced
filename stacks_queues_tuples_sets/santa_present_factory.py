from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

doll = 150
wooden_train = 250
teddy_bear = 300
bicycle = 400

presents = {'Bicycle': 0, 'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0}

for piece in range (len(materials), -1, -1):
    if len(materials) == 0:
        break
    elif len(magic) == 0:
        break
    total_magic_level = materials[-1] * magic[0]
    if total_magic_level == doll or total_magic_level == wooden_train or total_magic_level == teddy_bear or total_magic_level == bicycle:
        if total_magic_level == doll:
            presents['Doll'] += 1
        elif total_magic_level == wooden_train:
            presents['Wooden train'] += 1
        elif total_magic_level == teddy_bear:
            presents['Teddy bear'] += 1
        elif total_magic_level == bicycle:
            presents['Bicycle'] += 1
        materials.pop()
        magic.popleft()
    elif total_magic_level < 0:
        output = materials[-1] + magic[0]
        materials.pop()
        magic.popleft()
        materials.append(output)
    elif total_magic_level > 0 and (total_magic_level != doll or total_magic_level != wooden_train or total_magic_level != teddy_bear or total_magic_level != bicycle):
        magic.popleft()
        materials[-1] += 15
    elif materials[-1] == 0:
        materials.pop()
        if magic[0] == 0:
            magic.popleft()
    elif magic[0] == 0:
        magic.popleft()
        if materials[-1] == 0:
            materials.pop()

if (presents['Doll'] > 0 and presents['Wooden train'] > 0) or (presents['Teddy bear'] > 0 and presents['Bicycle'] > 0):
    print('The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')
if len(materials) != 0:
    materials_as_str = reversed([str(x) for x in materials])
    print(f"Materials left: {', '.join(materials_as_str)}")
if len(magic) != 0:
    magic_as_str = reversed([str(x) for x in magic])
    print(f"Magic left: {', '.join(magic_as_str)}")

sorted_presents = sorted(presents.items(), key=lambda kvp: kvp[0])

for (key, value) in sorted_presents:
    if value != 0:
        print(f'{key}: {value}')