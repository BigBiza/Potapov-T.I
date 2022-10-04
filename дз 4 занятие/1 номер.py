a=int(input('Введите число:'))
b=int(input('Введите число большее, чем предыдущее:'))
while b<a:
    b=int(input('Введите число большее, чем предыдущее:'))
while a<=b:
    print(a)
    a=a+1


