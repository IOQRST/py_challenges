def double_char(s):
    lst = []
    for i in s:
        lst.append(i * 2)
    return "".join(lst)


print(double_char("String"))
print(double_char("Hello World"))
print(double_char("1234!_ "))
