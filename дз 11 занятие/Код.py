import requests
import json
from tkinter import *


def clicked():
    name = txt.get()
    # Имечко чувачка, который мне нужен = 'Automattic'
    url = f'https://api.github.com/users/{name}'
    userdata = requests.get(url).json()

    jsn = {
        'company': userdata['company'],
        'created_at': userdata['created_at'],
        'email': userdata['email'],
        'id': userdata['id'],
        'name': userdata['name'],
        'url': userdata['url']
    }

    with open('Файл.json', 'a') as file:
        json.dump(jsn, file)


window = Tk()
window.title('Что-то типа окна :/')
window.geometry('500x69')
lbl = Label(window, text='Введите имечко чевачка, который Вам нужен: ')
lbl.grid(column=0, row=0)
txt = Entry(window, width=30)
txt.grid(column=1, row=0)
btn = Button(window, text='Тык!(чтобы сработало то, я написал)', command=clicked)
btn.grid(column=1, row=1)
lbl_2 = Label(window, text='', anchor='w')
lbl_2.grid(column=0, row=2)
window.mainloop()
