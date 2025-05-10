def find_deleted_number(arr, mixed_arr):
    lost_number = 0

    for i in arr:
        if i not in mixed_arr:
            lost_number = i

    return lost_number


print(find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]))
