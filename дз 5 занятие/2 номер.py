n=int(input('Введите число не меньшее 2:'))
if n>=2:
    for i in range(2,n+1):
        if n%i==0:
            print(i)
            break
else:
    print('Введено неподходящее число')
