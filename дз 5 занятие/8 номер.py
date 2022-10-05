a = int(input('Введите число:'))
s = 0
while a != 0:
    b = a
    a = int(input('Введите число:'))
    if a == b:
        s += 1
else:
    print(s)
