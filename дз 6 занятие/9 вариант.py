def poisk(text, slovo):
    s = text.count(slovo)
    print('Искомое слово втречается в тексте', s, 'раз')


txt = input('Введите текст: \n')
slv = input('Введите искомое слово:\n')
print(poisk(txt,slv))
