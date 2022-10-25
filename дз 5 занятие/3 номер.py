def stepen(n):
    l = 0
    j = 1
    while j <= n:
        j *= 2
        l += 1
    return l - 1, j // 2
a = int(input('Введите число:'))
print(stepen(a))
