from collections import deque

def stock_availability(flavours, cmd, *args):
    dequed_flavours = deque(flavours)
    if cmd == 'delivery':
        for el in args:
            dequed_flavours.append(el)
    elif cmd == 'sell':
        if len(args) != 0:
            if str(args[0]).isdigit():
                for i in range(args[0]):
                    dequed_flavours.popleft()
                return list(dequed_flavours)
            else:
                for value in args:
                    for flavour in flavours:
                        if value == flavour:
                            while value in flavours:
                                flavours.remove(value)
                return flavours
        elif len(args) == 0:
            dequed_flavours.popleft()
    return list(dequed_flavours)

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate", 'hui', 'bui'))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))