def count_by(x, n):
    tick = 1
    lst = []
    while len(lst) < n:
        if tick % x == 0:
            lst.append(tick)
        tick += 1

    return lst


print(count_by(1, 5))
print(count_by(2, 5))
print(count_by(3, 5))
print(count_by(50, 5))
print(count_by(100, 5))
