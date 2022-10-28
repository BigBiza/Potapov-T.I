def massiv(array, n):
    nepovt = []
    for i in range(n):
        for j in range(i+1, n):
            if array[i] == array[j]:
                nepovt.append(array[i])
    return nepovt


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
