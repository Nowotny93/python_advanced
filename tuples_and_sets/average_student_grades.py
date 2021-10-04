number_of_students = int(input())

dictionary = {}

for i in range(1, number_of_students + 1):
    student_grade = input().split()
    student = student_grade[0]
    grade = "{:.2f}".format(float(student_grade[1]))
    if student_grade[0] not in dictionary:
        dictionary[student] = []
        dictionary[student].append(grade)
    else:
        dictionary[student].append(grade)

for key, value in dictionary.items():
    print(f'{key} -> {(" ".join(value))} (avg: {"{:.2f}".format((sum(float(x) for x in value))/len(value))})')