def no_space(x):
    lst = []
    for i in x:
        if i != " ":
            lst.append(i)

    return "".join(lst)


print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
