clothes = input().split()
list_clothes = [int(x) for x in clothes]

capacity_of_rack = int(input())
stack = []
sum_racks = 1

reversed_list_clothes = reversed(list_clothes)
for num in reversed_list_clothes:
    if num <= capacity_of_rack:
        stack.append(num)
        if sum(stack) == capacity_of_rack:
            sum_racks += 1
            stack.clear()
        elif sum(stack) > capacity_of_rack:
            sum_racks += 1
            stack.clear()
            stack.append(num)

print(sum_racks)