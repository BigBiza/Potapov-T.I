def vivod(a, b):
    while b < a:
        b = int(input('Введите число большее, чем предыдущее:'))
    while a <= b:
        print(a)
        a += 1
c = int(input('Введите число:'))
d = int(input('Введите число большее, чем предыдущее:'))
print(vivod(c, d))
