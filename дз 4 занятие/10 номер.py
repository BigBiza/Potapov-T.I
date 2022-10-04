n=int(input('Введите число:'))
k=int(input('Введите число:'))
m=0
b=1
s=0
f=0
for i in range(n):
    s=s+m
    l=m+b
    m=b
    b=l
m=0
b=1
for j in range(k):
    f=f+m
    l=m+b
    m=b
    b=l
print(s-f)
