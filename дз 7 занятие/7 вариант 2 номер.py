def massiv(array, n):
    mxi = 0
    mni = 0
    for i in range(n):
        if array[i] > array[mxi]:
            mxi = i
        if array[i] < array[mni]:
            mni = i
    j = array[mni]
    array[mni] = array[mxi]
    array[mxi] = j
    return array


N = int(input('Введите число элемнтов массива:'))
arr = [int(input()) for i in range(N)]
print(arr)
print(massiv(arr, N))
