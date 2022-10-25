def zamena(text):
    s = 0
    for i in range(len(text)//2):
        if text[i] == 'п':
            s += 1
    text = text.replace('п', '*', s)
    return text, s


txt = input('Введите текст:')
print(zamena(txt))
