def massiv(array, n):
    sm = 0
    for i in range(n-1):
        if array[i] != 0:
            sm += array[i]
        else:
            array[i] = sm/n
    return array[n-1]


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
