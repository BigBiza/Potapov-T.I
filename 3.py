print('Введите возраст:')
age = int(input())
while (age < 0) or (age > 75):
    print('Введите более подходящий возраст:')
    age = int(input())
print('Введите своё имя:')
name = str(input())
while name == 'Иван':
    print('Нас не удовлетворяет Ваше имя, придумайте другое:')
    name = str(input())
if (age >= 16):
    print('Поздравляем вы поступили в ВГУИТ')
else:
    s = 16 - age
    if s <= 9:
        print('Приходи через ',s,' лет!')
    else:
        print('Сначала нужно окончить школу!')