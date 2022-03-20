from tkinter import *
"Установщик pack()"

root = Tk()
one = Label(root, text = 'ONE', bg = 'black', fg = 'yellow')
one.pack()

two = Label(root, text = 'TWO', bg = 'green', fg = 'red')
two.pack(fill = X)#объект будет растягиваться по оси х

three = Label(root, text = 'THREE', bg = 'black', fg = 'white')
three.pack(side = LEFT, fill = Y)#будет растягиваться по у


root.mainloop()