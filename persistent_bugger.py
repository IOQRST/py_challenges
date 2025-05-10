def persistence(n):
    if n <= 10:
        return 0
    else:
        counter = 1
        while True:
            t = []
            p = 1
            n = str(n)

            for i in n:
                t.append(int(i))

            for i in t:
                p *= i

            if p < 10:
                return counter
            else:
                counter += 1
                n = p


print(persistence(25))
