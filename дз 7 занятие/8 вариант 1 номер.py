def massiv(array, n):
    sm = 0
    pr = 1
    for i in range(n):
        sm += array[i]
        pr *= array[i]
    return sm, pr


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
