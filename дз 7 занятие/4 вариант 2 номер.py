def massiv(array, n):
    nechet = []
    for i in range(n):
        if array[i] % 2 != 0:
            nechet.append(array[i])
    if not nechet:
        return 'Нечётных элементов в исходном массиве нет!'
    return nechet


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
