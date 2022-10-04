n=int(input('Введите число:'))
s=0
m=1
for i in range(n):
    s=s+m**3
    m=m+1
print(s)
