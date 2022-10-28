def massiv(array, n):
    t = 0
    for i in range(n):
        if array[i] > array[t]:
            t = i
    return t


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
