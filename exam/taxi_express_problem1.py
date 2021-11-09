from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxis = [int(x) for x in input().split(', ')]

total_time = 0
end_of_trip = False
for customer in list(customers):
    if len(taxis) == 0:
        end_of_trip = True
        break
    last_taxi = taxis[-1]
    while last_taxi < customer:
        taxis.pop()
        if len(taxis) == 0:
            print('Not all customers were driven to their destinations')
            print(f'Customers left: {", ".join([str(x) for x in customers])}')
            exit()
        last_taxi = taxis[-1]
    else:
        if last_taxi >= customer:
            total_time += customer
            customers.popleft()
            taxis.pop()

if end_of_trip:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(x) for x in customers])}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')