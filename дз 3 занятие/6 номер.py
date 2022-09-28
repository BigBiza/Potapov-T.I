def board(a,c):
    return (8*c+8*a)%2
x=int(input('Введите номер первого столбца:'))
while x<1 or x>8:
    x=int(input('Число неправильное, попробуйте ещё раз:'))
y=int(input('Введите номер первой строки:'))
while y<1 or y>8:
    y=int(input('Число неправильное, попробуйте ещё раз:'))
z=int(input('Введите номер второго столбца:'))
while z<1 or z>8:
    z=int(input('Число неправильное, попробуйте ещё раз:'))
f=int(input('Введите номер второй строки:'))
while f<1 or f>8:
    f=int(input('Число неправильное, попробуйте ещё раз:'))
if board(x,y)==board(z,f):
    print('Да')
else:
    print('Нет')
