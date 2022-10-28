def massiv(array, n):
    plus = []
    minus = []
    for i in range(n):
        if array[i] < 0:
            minus.append(array[i])
        elif array[i] > 0:
            plus.append(array[i])
    return plus, minus


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
