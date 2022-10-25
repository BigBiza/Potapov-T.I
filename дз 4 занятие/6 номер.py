def factorial(n):
    s = 1
    m = 1
    for i in range(n):
        s = s*m
        m += 1
    print(s)
a = int(input('Введите число:'))
print(factorial(a))
