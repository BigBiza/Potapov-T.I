def sumfactorial(n):
    s = 1
    m = 0
    for i in range(1, n+1):
        s = s*i
        m += s
    print(m)
a=int(input('Введите число:'))
print(sumfactorial(a))
