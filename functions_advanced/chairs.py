from itertools import combinations

result = list(combinations(input().split(', '), int(input())))
for x, y in result:
    print(x, y, sep=',')