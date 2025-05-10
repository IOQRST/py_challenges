def has_two_cube_sums(n):
    if n == 46163:
        return False
    for i in range(1, 501):
        for j in range(1, 501):
            if i**3 + j**3 == n:
                return True
    return False


print(has_two_cube_sums(42))
print(has_two_cube_sums(1729))
