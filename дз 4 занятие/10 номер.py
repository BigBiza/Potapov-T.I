def fib(n):
    m = 0
    b = 1
    s = 0
    for i in range(n):
        s += m
        l = m + b
        m = b
        b = l
    return s
a = int(input('Введите число:'))
k = int(input('Введите число:'))
print(fib(a) - fib(k))
