def doviv(a, b):
    if a <= b:
        while a <= b:
            print(a)
            a += 1
    else:
        while b <= a:
            print(a)
            a -= 1
c = int(input('Введите число:'))
d = int(input('Введите число:'))
print(doviv(c, d))
