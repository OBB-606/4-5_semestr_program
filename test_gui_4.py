from tkinter import *
"Упаковщик grid"

root = Tk()


label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row = 0, column = 0, sticky = E)#Sticky делает выравнивание объекта по какой-либо стороне,
#обозначающейся какой-либо стороной света, в данном случае надо было выровнять по правой границе,
#значит, ВОСТОК
label_2.grid(row = 1, column = 0)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

check_button = Checkbutton(root, text = "ОСтаться в системе")
check_button.grid(columnspan = 2)

root.mainloop()