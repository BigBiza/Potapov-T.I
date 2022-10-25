def delete(text):
    s = 0
    for i in range(len(text)):
        if text[i] == 'а':
            s += 1
    text = text.replace('а', '', s)
    return text, s


txt = input('Введите текст:')
print(delete(txt))
