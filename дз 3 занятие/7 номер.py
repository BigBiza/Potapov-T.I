def year(z):
    if (z%4==0) and not (z%100==0) or (z%400==0):
        return ('Да')
    else:
        return('Нет')
y=int(input('Введите желаемый год:'))
print(year(y))


