random_number = int(input())

stack = []

for i in range (1, random_number + 1):
    command = input()
    if '1' in command:
        command_splt = command.split()
        number_to_push = int(command_splt[1])
        stack.append(number_to_push)
    elif '2' in command:
        if len(stack) > 0:
            stack.pop()
    elif '3' in command:
        if len(stack) > 0:
            print(max(stack))
    elif '4' in command:
        if len(stack) > 0:
            print(min(stack))

reversed_stack = []
for z in range(len(stack)):
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))