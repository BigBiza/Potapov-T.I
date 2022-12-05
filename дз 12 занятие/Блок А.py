def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)


X = int(input('Введите X: '))
N = int(input('Введите N: '))
print(X**N / fac(N))
