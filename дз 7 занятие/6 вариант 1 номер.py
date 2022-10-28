def massiv(array):
    mn = 0
    mx = 0
    sm = 0
    for i in range(10):
        sm += array[i]
    sr = sm / 10
    for i in range(10):
        if array[i] < sr:
            mn += 1
        if array[i] > sr:
            mx += 1
    return mn, mx


arr = [int(input()) for i in range(10)]
print(arr)
print(massiv(arr))
