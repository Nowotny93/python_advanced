def age_assignment(*args, **kwargs):
    dictionary = {}
    for name in args:
        for letter, age in kwargs.items():
            if letter == name[0]:
                dictionary[name] = age
    return dictionary

print(age_assignment("Peter", "George", G=26, P=19))