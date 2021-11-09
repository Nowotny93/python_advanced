from collections import deque

def list_manipulator(random_list, arg1, arg2, *args):
    if arg1 == 'add' and arg2 == 'beginning':
        return list(args) + random_list
    elif arg1 == 'add' and arg2 == 'end':
        return random_list + list(args)
    elif arg1 == 'remove' and arg2 == 'beginning':
        if len(args) != 0:
            deque_random_list = deque(random_list)
            for i in range (0, *args):
                deque_random_list.popleft()
            return list(deque_random_list)
        else:
            deque_random_list = deque(random_list)
            deque_random_list.popleft()
            return list(deque_random_list)
    elif arg1 == 'remove' and arg2 == 'end':
        if len(args) != 0:
            for i in range(0, *args):
                random_list.pop()
            return random_list
        else:
            random_list.pop()
            return random_list

print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))