file = open("input.txt", 'r')

count = -1
for line in file:
    count += 1
    if count % 2 == 0:
        if '.' in line or ',' in line or '!' in line or '?' in line or '-' in line:
            new_line = line.replace('.', '@')
            new_line = new_line.replace(',', '@')
            new_line = new_line.replace('!', '@')
            new_line = new_line.replace('?', '@')
            new_line = new_line.replace('-', '@')
            listed_line = new_line.split()
            reversed_listed_line = ' '.join(reversed(listed_line))
            print(reversed_listed_line)