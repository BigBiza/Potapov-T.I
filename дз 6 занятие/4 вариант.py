def zamena(text):
    s = 0
    for i in range(len(text)):
        if text[i] == 'а':
            s += 1
    text = text.replace('а', 'о', s)
    return text, s, len(text)


txt = input('Введите текст:')
print(zamena(txt))
