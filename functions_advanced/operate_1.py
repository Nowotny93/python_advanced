from functools import reduce

def operate (arg1, *rest_args):
    return reduce (lambda x, y: eval(f"{x} {arg1} {y}"), rest_args)