def ch(n,m,k):
    if ((k%n==0) or (k%m==0)) and (k<m*n):
        return ('Да')
    else:
        return('Нет')
n=int(input('Введите число:'))
m=int(input('Введите число:'))
k=int(input('Введите количество требуемых долек:'))
print(ch(n,m,k))
