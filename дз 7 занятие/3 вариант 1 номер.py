def massiv(array, n):
    sm = 0
    for i in range(n):
        if i % 2 == 0:
            sm += array[i]
    return array, sm


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
