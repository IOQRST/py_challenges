def remove_smallest(numbers):
    temp_lst = numbers.copy()
    if len(temp_lst) == 0:
        return []
    else:
        temp_lst.remove(min(temp_lst))
        return temp_lst


print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([1, 2, 3, 1, 1]))
print(remove_smallest([]))
