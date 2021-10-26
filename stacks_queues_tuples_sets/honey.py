from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

for piece in range (0, len(bees)):
    if len(nectar) == 0:
        break
    while bees[0] > nectar[-1]:
            nectar.pop()
            if len(nectar) == 0:
                break
    if len(nectar) == 0:
        break
    else:
        if symbols[0] == '+':
            total_honey += abs(bees[0] + nectar[-1])
        elif symbols[0] == '-':
            total_honey += abs(bees[0] - nectar[-1])
        elif symbols[0] == '*':
            total_honey += abs(bees[0] * nectar[-1])
        elif symbols[0] == '/':
            total_honey += abs(bees[0] / nectar[-1])
        bees.popleft()
        nectar.pop()
        symbols.popleft()

print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(x) for x in nectar])}')