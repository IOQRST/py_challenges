lst = [input() for _ in '...']
count = 0
for i in range(len(lst)):
    lst[i] = int(lst[i][-2: ])

for i in lst:
    if i < 20:
        count += 1
print(count)