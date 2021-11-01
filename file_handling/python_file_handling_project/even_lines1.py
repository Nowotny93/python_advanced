import re

file = open("input.txt", 'r')

for idx, line in enumerate(file.readlines()):
    if idx % 2 != 0:
        continue

    line = re.sub(r'[-,.!?]', '@', line)
    line = ' '.join(reversed(line.split()))
    print(line.strip())