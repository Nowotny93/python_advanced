from functools import reduce

def operate (arg1, *rest_args):
    if arg1 == '+':
        return reduce (lambda x, y: x + y, rest_args)
    elif arg1 == '-':
        return reduce(lambda x, y: x - y, rest_args)
    elif arg1 == '*':
        return reduce(lambda x, y: x * y, rest_args)
    else:
        return reduce(lambda x, y: x / y, rest_args)

print(operate('+', 1, 2, 3))