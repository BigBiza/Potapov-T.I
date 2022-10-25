def fibonachi(n):
    m = 0
    k = 1
    s = 0
    for i in range(n):
        s += m
        j = m + k
        m = k
        k = j
    print(s)
a=int(input('Введите число:'))
print(fibonachi(a))
