def nod(n):
    if n >= 2:
        for i in range(2, n+1):
            if n % i == 0:
                return i
                break
    else:
        return 'Введено неподходящее число'
a = int(input('Введите число не меньшее 2:'))
print(nod(a))
