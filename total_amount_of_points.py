def points(games):
    total = 0
    for i in games:
        if int(i[0]) == int(i[2]):
            total += 1
        elif int(i[0]) > int(i[2]):
            total += 3
        elif int(i[0]) < int(i[2]):
            continue

    return total


print(points(["1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"]))
