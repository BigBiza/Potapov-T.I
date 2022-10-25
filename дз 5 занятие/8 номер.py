def ravn(a):
    s = 0
    l = 0
    while a != 0:
        b = a
        a = int(input('Введите число:'))
        if a == b:
            s += 1
        else:
            if s > l:
                l = s
                s = 0
    return l
n = int(input('Введите число:'))
print(ravn(n))
