def kubesum(n):
    s = 0
    m = 1
    for i in range(n):
        s = s + m ** 3
        m = m+1
    print(s)
a = int(input('Введите число:'))
print(kubesum(a))
