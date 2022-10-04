a=int(input('Введите число:'))
b=int(input('Введите число меньшее, чем предыдущее:'))
while b>=a:
    b=int(input('Введите число меньшее, чем предыдущее:'))
while a>b:
    if not a%2==0:
        print(a)
        a=a-1
    else:
        a=a-1
