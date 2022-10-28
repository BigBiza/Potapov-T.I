def massiv(array, brray, n):
    c = []
    for i in range(n):
        c.append(array[i])
    array = []
    for i in range(n):
        array.append(brray[i])
    brray = []
    for i in range(n):
        brray.append(c[i])
    return array, brray


N = int(input('Введите число элемнтов массива:'))
arr = [int(input('Элемент массива А:')) for i in range(N)]
brr = [int(input('Элемент массива B:')) for i in range(N)]
print(massiv(arr, brr, N))
