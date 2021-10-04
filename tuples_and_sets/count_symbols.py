random_word = list("".join(input()))
random_word.sort()

gathered_characters = []

for ch in random_word:
    occurences = random_word.count(ch)
    if ch in gathered_characters:
        continue
    else:
        gathered_characters.append(ch)
        print(f'{ch}: {random_word.count(ch)} time/s')