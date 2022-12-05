def maxel():
    n = int(input('Введите элемент последовательности: '))
    if n == 0:
        return 0
    m = maxel()
    if n > m:
        return n
    else:
        return m


print('Наибольшее число в последовательности:', maxel())
