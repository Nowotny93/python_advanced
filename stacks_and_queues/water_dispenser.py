from collections import deque
queue = deque()

quantity_water = int(input())
command = input()

while command != 'Start':
    queue.append(command)
    command = input()

random = input()

while random != "End":
    if len(random) == 1:
        liters = int(random)
        if liters <= quantity_water:
            print(f'{queue.popleft()} got water')
            quantity_water -= liters
        else:
            print(f'{queue[0]} must wait')
            queue.popleft()
    elif len(random) != 1:
        random_splt = random.split()
        liters_to_add = int(random_splt[1])
        quantity_water += liters_to_add
    random = input()
if quantity_water < 0:
    print('0 liters left')
else:
    print(f'{quantity_water} liters left')