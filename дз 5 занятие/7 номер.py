def sravn(a):
    b = a
    s = 0
    while a != 0:
        a = int(input('Введите число:'))
        if a > b:
            s += 1
        b = a
    else:
        return s
n = int(input('Введите число:'))
print(sravn(n))
