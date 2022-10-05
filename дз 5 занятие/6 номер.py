a = int(input('Введите число:'))
s = 0
b = a
while a != 0:
    s += 1
    a = int(input('Введите число:'))
    b += a
else:
    print('Среднее арифметическое введеных чисел =',b / s)
