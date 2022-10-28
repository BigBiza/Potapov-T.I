def massiv(array, n):
    for i in range(n):
        if array[i] < 15:
            array[i] *= 2
    return array


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
