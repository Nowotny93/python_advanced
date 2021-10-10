from collections import deque

queue = deque()
food_quantity = int(input())
orders = input().split()

for num in orders:
    queue.append(int(num))

print(max(queue))

for ordered_food in orders:
    if int(ordered_food) <= food_quantity:
        queue.popleft()
        food_quantity -= int(ordered_food)
    else:
        list_queue = list(queue)
        str_queue = [str(x) for x in list_queue]
        print(f'Orders left: {" ".join(str_queue)}')
        exit()

print('Orders complete')