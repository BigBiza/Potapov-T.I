def nod_k(a, b):
    nok = a * b
    while not a == b:
        if a > b:
            a -= b
        else:
            b -= a
    nok //= a
    return a, b, nok


x = int(input('Введите первое натуральное число:'))
z = int(input('Введите второе натуральное число:'))
print(nod_k(x, z))
