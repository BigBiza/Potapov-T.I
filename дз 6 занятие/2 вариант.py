def zamena(text):
    s = 0
    for i in range(len(text)):
        if text[i] == ':':
            s += 1
    text = text.replace(':', '%')
    return text, s


txt = input('Введите текст:')
print(zamena(txt))
