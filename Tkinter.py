from tkinter import *
from tkinter import ttk

import calculator

window = Tk()
window.title('Калькулятор вычисления выслуги лет')
window.geometry('400x300')


def receive_text():
    result = entry.get()
    try:
        if result.isdigit():
            print(result)
            print('Done date')
    except:
        print('введеные неверные данные')



entry = ttk.Entry()
entry.pack()

btn = ttk.Button(text='Выполнить', command=receive_text)
btn.pack()


window.mainloop()