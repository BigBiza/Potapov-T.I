def hours(n):
    return (n//60)%24, n%60

n=int(input('Введите число:'))
h,minutes=hours(n)
print(h,":",minutes)
