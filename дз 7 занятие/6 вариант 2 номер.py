def massiv(array):
    sm = 0
    for i in range(10):
        if array[i] > 5:
            sm += array[i]
    return sm


arr = [int(input()) for i in range(10)]
print(arr)
print(massiv(arr))
