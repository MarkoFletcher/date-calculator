from tkinter import *
from calculator import *
from datetime import datetime
from tkinter import messagebox


window = Tk()
window.title('Калькулятор вычисления выслуги лет')
window.geometry('400x300')


def open_info():
    messagebox.showerror(title="Ошибка",
    message="Ввод некоректных данных формата даты:\nВведите дату в формате XX.XX.XXXX")


def receive_text():
    try:
        entry_result = datetime.strptime(entry.get(), '%d.%m.%Y')
        print(entry_result)
    except:
        open_info()


lbl = Label(text='Введите дату начала службы')
lbl.pack()

entry = Entry()
entry.pack()

btn = Button(text='Выполнить', command=receive_text)
btn.pack()


window.mainloop()