def delete_nth(order, max_e):
    res = []
    for i in order:
        if res.count(i) < max_e:
            res.append(i)
    return res


print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))
print(delete_nth([1, 1, 1, 1, 1], 5))
print(delete_nth([12, 39, 19, 39, 39, 19, 12], 1))
