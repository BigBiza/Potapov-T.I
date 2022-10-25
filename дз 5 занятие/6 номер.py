def srarif(a):
    s = 0
    b = a
    while a != 0:
        s += 1
        a = int(input('Введите число:'))
        b += a
    else:
        print('Среднее арифметическое введеных чисел =', b / s)
n = int(input('Введите число:'))
print(srarif(n))
