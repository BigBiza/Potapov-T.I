def matrix(n, ar):
    mx = []
    mn = []
    for i in range(n):
        mn.append(min(ar[i]))
        mx.append(max(ar[i]))
    str(mn)
    str(mx)
    file = open('Потапов_У-222_vivod.txt', 'w')
    file.write(str(mn))
    file.write(str(mx))
    file.close()
    return mn, mx


a = int(input('Введите число строк и столбцов:'))
mat = []
file = open('Потапов_У-222_vvod.txt', 'r')
for line in file:
    mat.append([int(x) for x in line.split()])
file.close()
print(matrix(a, mat))
