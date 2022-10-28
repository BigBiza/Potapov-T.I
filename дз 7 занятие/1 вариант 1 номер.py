def massiv(array, n):
    yarra = [array[n-1]]
    for i in range(n-1):
        yarra.insert(1, array[i])
    return yarra, array[n-1]


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
