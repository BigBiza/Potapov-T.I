def vvd(a,b):
    while b > a:
        b = int(input('Введите число меньшее, чем предыдущее:'))
    while a >= b:
        if not a % 2 == 0:
            print(a)
            a -= 1
        else:
            a -= 1
c = int(input('Введите число:'))
d = int(input('Введите число меньшее, чем предыдущее:'))
print(vvd(c,d))
