from math import floor


def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        p0 = floor(p0 + p0 * (percent / 100) + aug)
        count += 1

    return count


print(nb_year(1500, 5, 100, 5000))
print(nb_year(1000, 2, 100, 5000))
