from collections import deque

bombs = deque(int(x) for x in input().split(', '))
casings = [int(x) for x in input().split(', ')]

dict_bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

for bomb in list(bombs):
    casing = casings[-1]
    output = bomb + casing
    while output != 40 and output != 60 and output != 120:
        casing -= 5
        output = bomb + casing
    if output == 40:
        dict_bombs['Datura Bombs'] += 1
        bombs.popleft()
        casings.pop()
    elif output == 60:
        dict_bombs['Cherry Bombs'] += 1
        bombs.popleft()
        casings.pop()
    elif output == 120:
        dict_bombs['Smoke Decoy Bombs'] += 1
        bombs.popleft()
        casings.pop()
    if (dict_bombs['Datura Bombs'] >= 3 and dict_bombs['Cherry Bombs'] >= 3 and dict_bombs['Smoke Decoy Bombs'] >= 3) \
        or len(bombs) == 0 or len(casings) == 0:
        break

if (dict_bombs['Datura Bombs'] >= 3 and dict_bombs['Cherry Bombs'] >= 3 and dict_bombs['Smoke Decoy Bombs'] >= 3):
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bombs) == 0:
    print('Bomb Effects: empty')
else:
    print(f'Bomb Effects: {", ".join([str(x) for x in bombs])}')

if len(casings) == 0:
    print('Bomb Casings: empty')
else:
    print(f'Bomb Casings: {", ".join([str(x) for x in casings])}')

for (key, value) in sorted(dict_bombs.items(), key = lambda kvp: kvp[0]):
    print(f'{key}: {value}')