def nsum(n):
    s = 0
    for i in range(n):
        s += int(input())
    print(s)
a = int(input('Введите количество  чисел:'))
print(nsum(a))
