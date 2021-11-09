nums = [int(x) for x in input().split(', ')]
index_task_intr = int(input())

task_intr = nums[index_task_intr]
clock_cycles = 0
for num in sorted(nums):
    if num != task_intr:
        clock_cycles += num
    else:
        if nums.count(num) > 1:
            clock_cycles += num
            index_of_num = nums.index(num)
            nums.pop(index_of_num)
            continue
        else:
            clock_cycles += num
            break

print(clock_cycles)