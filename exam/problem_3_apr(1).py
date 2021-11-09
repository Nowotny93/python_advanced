def flights(*args):
    dict_dest = {}
    finish_index = args.index('Finish')
    for i in range (3, finish_index + 3, 2):
        city = args[i - 3]
        people = args[i - 2]
        if city not in dict_dest:
            dict_dest[city] = people
        else:
            dict_dest[city] += people
    return dict_dest

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))