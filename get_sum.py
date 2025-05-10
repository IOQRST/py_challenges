def get_sum(a, b):
    if a == b:
        return a
    elif a > b:
        a, b = b, a
        re = [x for x in range(a, b + 1)]
        return sum(re)
    else:
        re = [x for x in range(a, b + 1)]
        return sum(re)


print(get_sum(1, 0))  # 1
print(get_sum(1, 2))  # 3
print(get_sum(0, 1))  # 1
print(get_sum(1, 1))  # 1
print(get_sum(-1, 0))  # -1
print(get_sum(0, -1))  # -1
print(get_sum(-1, 2))  # 2
