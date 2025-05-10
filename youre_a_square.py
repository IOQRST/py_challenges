def is_square(n):
    return False if n < 0 else (n**0.5).is_integer()


print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))
