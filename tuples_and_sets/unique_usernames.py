usernames = int(input())

usernames_set = set([])

for i in range (1, usernames + 1):
    username = input()
    if username not in usernames_set:
        usernames_set.add(username)

for name in usernames_set:
    print(name)