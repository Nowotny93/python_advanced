from collections import deque

males = [int(x) for x in input().split() if int(x) > 0]
females = [int(x) for x in input().split() if int(x) > 0]

for m in males:
    if m % 25 == 0:
        m_index = males.index(m)
        males.pop(m_index)
        try:
            males.pop(m_index + 1)
        except:
            IndexError

for f in females:
    if f % 25 == 0:
        f_index = females.index(f)
        females.pop(f_index)
        try:
            females.pop(f_index + 1)
        except:
            IndexError

females = deque(females)
successful_matches = 0
for idx in range(len(males) - 1, -1, -1):
    if len(females) == 0:
        break
    for female in list(females):
        if female == males[idx]:
            males.pop()
            females.popleft()
            successful_matches += 1
            break
        elif female != males[idx]:
            females.popleft()
            males[idx] -= 2
            if males[idx] <= 0:
                males.pop()
                break

print(f'Matches: {successful_matches}')

if len(males) == 0:
    print("Males left: none")
else:
    print(f'Males left: {", ".join(str(x) for x in list(reversed(males)))}')

if len(females) == 0:
    print("Females left: none")
else:
    print(f'Females left: {", ".join(str(x) for x in females)}')