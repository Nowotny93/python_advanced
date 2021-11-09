from collections import deque

def datura_bombs(dictionary, bs, cs):
    dictionary['Datura Bombs'] += 1
    bs.popleft()
    cs.pop()

def cherry_bombs(dictionary, bs, cs):
    dictionary['Cherry Bombs'] += 1
    bs.popleft()
    cs.pop()

def smoke_bombs(dictionary, bs, cs):
    dictionary['Smoke Decoy Bombs'] += 1
    bs.popleft()
    cs.pop()

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
        datura_bombs(dict_bombs, bombs, casings)
    elif output == 60:
        cherry_bombs(dict_bombs, bombs, casings)
    elif output == 120:
        smoke_bombs(dict_bombs, bombs, casings)
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