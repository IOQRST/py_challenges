def past(h, m, s):
    return (((h * 60) + m) * 60 + s) * 1000


print(past(0, 1, 1))
