def sranb(text):
    s = 0
    l = 0
    for i in range(len(text)):
        if text[i] == 'н':
            s += 1
        else:
            if s > l:
                l = s
                s = 0
    text = text.replace('!', '.')
    return text, l


txt = input('Введите текст:')
print(sranb(txt))
