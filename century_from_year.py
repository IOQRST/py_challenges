def century(year):
    return year // 100 if year % 100 == 0 else year // 100 + 1


print(century(1705))
print(century(1700))
