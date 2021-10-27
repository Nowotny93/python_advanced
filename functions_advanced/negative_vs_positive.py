numbers = input().split()

sum_negative = 0
sum_positive = 0

for i in numbers:
    int_number = int(i)
    if int_number < 0:
        sum_negative += int_number
    else:
        sum_positive += int_number

print(sum_negative)
print(sum_positive)
if sum_positive > abs(sum_negative):
    print('The positives are stronger than the negatives')
elif sum_positive < abs(sum_negative):
    print('The negatives are stronger than the positives')