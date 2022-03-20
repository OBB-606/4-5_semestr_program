from tkinter import *
from tkinter import messagebox

root = Tk()

def btn_click():
    login = loginInput.get()
    loginInput.delete(0,END)#очищает поле логина
    password = passwordInput.get()
    passwordInput.delete(0,END)#очищает поле пароля
    info_str = f'Data: {login, password}'
    messagebox.showinfo(title = 'SomeText', message = info_str)
    #window with Error
    #messagebox.showerror(title ='', message='fuck you!')

root['bg'] = '#000000'# фон окна
root.title('Motherfucker')#название окна
root.wm_attributes('-alpha', 0.9)#Прозрачность окна
root.geometry('300x250')
root.resizable(width=True, height= True)#изменение размера

#canvas = Canvas(root, height = 300, width = 250)#позволяет рисовать
#canvas.pack()

frame = Frame(root, bg = 'yellow')#рамка
frame.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.7)#указывание размеров объекта frame
            #смещение по x(в %), смещение по y(в %),занимаемая ширина окна (в %)б занимаемая высота окна (в %)

title = Label(frame, text = 'You fucking Motherfucker!', bg = 'orange', font = 40)
title.pack()

loginInput = Entry(frame, bg = 'lightblue')
loginInput.pack()
passwordInput = Entry(frame, bg = 'lightgreen', show= '*')
passwordInput.pack()
btn = Button(frame, text = 'Press', bg = 'green', command = btn_click)
btn.pack(side = RIGHT)
root.mainloop()