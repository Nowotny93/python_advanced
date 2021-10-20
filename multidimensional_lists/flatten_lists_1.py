lists = [x for x in input().split('|')]
lists_joined = ', '.join(lists)
lists_without_space = lists_joined.strip()
print(lists_without_space)