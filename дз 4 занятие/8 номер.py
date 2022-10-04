m=''
n=int(input('Введите число от 1 до 9:'))
if 0<n<=9:
    for i in range(1,n+1):
        m=m+str(i)
        print(m)
else:
    print('Введено неправильно число')
