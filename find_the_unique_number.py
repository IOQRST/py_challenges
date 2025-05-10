def find_unique(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            continue
        elif i == 0:
            return arr[i]
        else:
            return arr[i + 1]


print(find_unique([1, 1, 1, 2, 1, 1]))
print(find_unique([0, 0, 0.55, 0, 0]))
print(find_unique([3, 10, 3, 3, 3]))
print(find_unique([2, 2, 2, 2, 1]))
