def get_middle(s):
    position = len(s) // 2
    if len(s) % 2 == 0:
        return f"{s[position - 1]}{s[position]}"
    else:
        return f"{s[position]}"


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
