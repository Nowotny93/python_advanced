def flights(*args, ):
    dict_destinations = {}
    for idx, city in enumerate(args):
        if str(city) == 'Finish':
            break
        elif not str(city).isdigit():
            if city not in dict_destinations:
                dict_destinations[city] = 0
        else:
            needed_city = args[idx - 1]
            dict_destinations[needed_city] += int(city)
    return dict_destinations

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))