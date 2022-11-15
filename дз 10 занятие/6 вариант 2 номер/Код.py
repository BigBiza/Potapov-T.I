def matrix(n, ar):
    mx = ar[0][0]
    mi = mj = 0
    for i in range(n):
        if (ar[i][i] > mx) or (ar[i][n-1-i] > mx):
            mx = ar[i][i]
            mi, mj = i, i
    ar[mi][mj], ar[n//2][n//2] = ar[n//2][n//2], ar[mi][mj]
    str(ar)
    file = open('Потапов_У-222_vivod.txt', 'w')
    file.write(str(ar))
    file.close()
    return ar


a = int(input('Введите нечетное число строк и столбцов:'))
while a % 2 == 0:
    a = int(input('Введите НЕЧЕТНОЕ число строк и столбцов:'))
mat = []
file = open('Потапов_У-222_vvod.txt', 'r')
for line in file:
    mat.append([int(x) for x in line.split()])
file.close()
print(matrix(a, mat))
