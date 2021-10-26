import math

expression = input().split()

random_stack = []

for el in expression:
    if el != '*' and el != '-' and el != '+' and el != '/':
        random_stack.append(el)
    else:
        random_stack = [int(x) for x in random_stack]
        if el == '+':
            result_sum = sum(random_stack)
            random_stack = [result_sum]
        elif el == '-':
            result_deduction = random_stack[0]
            for i in range (1, len(random_stack)):
                result_deduction -= random_stack[i]
            random_stack.clear()
            random_stack.append(result_deduction)
        elif el == '*':
            result_multiplication = random_stack[0]
            for z in range (1, len(random_stack)):
                result_multiplication *=  random_stack[z]
            random_stack.clear()
            random_stack.append(result_multiplication)
        elif el == '/':
            result_division = random_stack[0]
            for y in range (1, len(random_stack)):
                result_division /= random_stack[y]
            random_stack.clear()
            random_stack.append(math.floor(result_division))

random_stack_as_str = [str(x) for x in random_stack]
print(''.join(random_stack_as_str))