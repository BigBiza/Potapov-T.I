def matrix(n, ar):
    mx = []
    mn = []
    for i in range(n):
        mn.append(min(ar[i]))
        mx.append(max(ar[i]))
    return mn, mx


a = int(input('Введите число строк и столбцов:'))
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
