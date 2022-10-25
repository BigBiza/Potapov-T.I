def slova(text):
    s = 0
    for i in range(len(text)):
        if (text[i] == 'е') and (text[i - 1] == ' '):
            s += 1
    print('Количество слов, начинающихся на "е", равно', s)


txt = ' ' + input('Введите текст:')
print(slova(txt))
