a=int(input('Введите число:'))
b=int(input('Введите число:'))
if a<=b:
    while a<=b:
        print(a)
        a=a+1
else:
    while b<=a:
        print(a)
        a=a-1
