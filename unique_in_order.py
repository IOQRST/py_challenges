def unique_in_order(sequence):
    tt = []

    if len(sequence) == 0:
        return []

    for i in range(len(sequence)):
        if i == len(sequence) - 1:
            break
        if sequence[i] != sequence[i + 1]:
            tt.append(sequence[i])

    tt.append(sequence[-1])

    return tt


print(unique_in_order("AAAABBBCCDAABBB"))  # ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order("ABBCcAD"))  # ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1, 2, 2, 3, 3]))  # [1, 2, 3]
print(unique_in_order((1, 2, 2, 3, 3)))  # [1, 2, 3]
