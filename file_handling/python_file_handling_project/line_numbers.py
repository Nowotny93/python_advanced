import re

with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

all_letters = 0
for idx, line in enumerate(lines):
    all_punct_marks = len(re.findall(r"[-,.!?']", line))
    all_letters = len(re.findall(r"[a-zA-Z]", line))
    print(f'Line {idx + 1}: {line} ({all_letters})({all_punct_marks})')