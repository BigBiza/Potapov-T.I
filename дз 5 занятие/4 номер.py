def sport(x, y):
    d = 1
    while x < y:
        x *= 1.1
        d += 1
    return d
a = int(input('Введите, сколько километров пробежал спортсмен в первый день:'))
b = int(input('Введите, сколько ему требуется пробежать:'))
print(sport(a,b))
