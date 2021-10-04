random_numbers = input().split()
random_numbers_int = [float(x) for x in random_numbers]
t = (random_numbers_int)
gathered_numbers = []

for i in t:
    occurences = t.count(i)
    if i in gathered_numbers:
        continue
    else:
        gathered_numbers.append(i)
        print(f'{i} - {occurences} times')