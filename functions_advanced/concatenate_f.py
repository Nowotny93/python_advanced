def concatenate(*args):
    output = ''
    for el in args:
        output += el
    return output

print(concatenate("Soft", "Uni", "Is", "Great", "!"))