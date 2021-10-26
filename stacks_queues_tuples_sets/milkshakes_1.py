from collections import deque

chocolates = input().split(', ')
milk_cups = deque(input().split(', '))
enough_milkshakes = False
milkshakes = 0

for piece in range (len(chocolates) - 1, -1, -1):
    if chocolates[piece][0] == '-' or chocolates[piece][0] == '0':
        chocolates.pop(piece)
        if len(chocolates) == 0:
            break
    elif milk_cups[0][0] == '-' or milk_cups[0][0] == '0':
        milk_cups.popleft()
        if len(milk_cups) == 0:
            break
    elif chocolates[piece] == milk_cups[0]:
        chocolates.pop(piece)
        milk_cups.popleft()
        milkshakes += 1
        if milkshakes == 5:
            enough_milkshakes = True
            break
    elif chocolates[piece] != milk_cups[0]:
        milk_cups.append(milk_cups[0])
        milk_cups.popleft()
        chocolates[piece] = int(chocolates[piece]) - 5

if enough_milkshakes:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if len(chocolates) != 0:
    choco_as_str = [str(x) for x in chocolates]
    print(f"Chocolate: {', '.join(choco_as_str)}")
else:
    print('Chocolate: empty')
if len(milk_cups) != 0:
    milk_as_str = [str(x) for x in milk_cups]
    print(f"Milk: {', '.join(milk_as_str)}")
else:
    print('Milk: empty')