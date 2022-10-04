n=int(input('Введите число:'))
m=0
k=1
s=0
for i in range(n):
    s=s+m
    j=m+k
    m=k
    k=j
print(s)
