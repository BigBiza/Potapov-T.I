def schet(text):
    s = 0
    for i in range(len(text)):
        if text[i] == ' ':
            s += 1
    print('Количество слов в данной строке равно', s)


txt = input('Введите текст: \n') + ' '
print(schet(txt))
