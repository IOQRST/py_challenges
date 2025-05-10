def solution(string):
    lst = []
    for i in range(len(string) - 1, -1, -1):
        lst.append(string[i])
    return "".join(lst)


print(solution("world"))
print(solution("hello"))
print(solution(""))
print(solution("h"))
