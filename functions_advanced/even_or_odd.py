def even_odd(*args):
    if args[-1] == 'even':
        args_as_list = list(args)
        args_as_list.pop()
        even_numbers = [x for x in args_as_list if int(x) % 2 == 0]
        return even_numbers
    else:
        args_as_list = list(args)
        args_as_list.pop()
        odd_numbers = [x for x in args_as_list if int(x) % 2 != 0]
        return odd_numbers

print(even_odd(1, 2, 3, 4, 5, 6, "odd"))