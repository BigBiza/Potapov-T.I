def kolvo(a):
    s = 0
    while a < 0:
        a = int(input('Попробуйте снова:'))
    while a >= 0:
        if a == 0:
            print('Количество положительных чисел в последовательности равно ', s)
            break
        s += 1
        a = int(input('Введите положительное число:'))
        while a < 0:
            a = int(input('Попробуйте снова:'))
n = int(input('Введите положительное число:'))
print(kolvo(n))
