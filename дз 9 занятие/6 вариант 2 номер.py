def matrix(n, ar):
    mx = ar[0][0]
    mi = mj = 0
    for i in range(n):
        if (ar[i][i] > mx) or (ar[i][n-1-i] > mx):
            mx = ar[i][i]
            mi, mj = i, j
    ar[mi][mj], ar[n//2][n//2] = ar[n//2][n//2], ar[mi][mj]
    return ar


a = int(input('Введите нечетное число строк и столбцов:'))
while a % 2 == 0:
    a = int(input('Введите НЕЧЕТНОЕ число строк и столбцов:'))
mat = []
for i in range(a):
    bat = []
    for j in range(a):
        bat.append((int(input('Введите элемент матрицы:'))))
    mat.append(bat)
for i in range(a):
    for j in range(a):
        print(mat[i][j], end=' ')
    print()
print(matrix(a, mat))
