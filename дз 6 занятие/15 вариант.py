def slova(text):
    s = 0
    for i in range(len(text)):
        if text[i] == 'т':
            s += 1
    return s


txt = input('Введите текст:')
print(slova(txt))
