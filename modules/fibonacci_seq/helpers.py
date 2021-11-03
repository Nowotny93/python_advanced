def generate_sequence(n):
    seq = [0, 1]
    for el in range (2, n):
        seq.append(seq[-2] + seq[-1])
    str_sequence = [str(x) for x in seq]
    return seq

def find_number(num, seq):
    if num in seq:
        return seq.index(num)
    return f'The number {num} is not in the sequence'