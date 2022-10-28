def massiv(array, n):
    minusp = []
    for i in range(n-1):
        if (array[i] == array[i+1]) and (array[i] < 0):
            minusp.append(array[i])
            minusp.append(array[i+1])
    return minusp


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
