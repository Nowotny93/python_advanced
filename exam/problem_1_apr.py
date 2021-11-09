from collections import deque

pizza_orders = deque(int(x) for x in input().split(', ') if int(x) > 0 and int(x) < 11)
employees = [int(x) for x in input().split(', ')]

total_pizzas = 0
while pizza_orders and employees:
    pizza_order = pizza_orders[0]
    employee = employees[-1]

    if pizza_order <= employee:
        total_pizzas += pizza_order
        pizza_orders.popleft()
        employees.pop()
    elif pizza_order > employee:
        pizza_orders[0] -= employee
        total_pizzas += employee
        employees.pop()

if len(pizza_orders) == 0:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(str(x) for x in employees)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')