from tkinter import *
"Организация главного окна"
root  = Tk()

top_frame = Frame(root)#верхняя область
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

button_1 = Button(top_frame, text = "button_1", bg = 'red', fg = 'blue')
button_2 = Button(top_frame, text = "button_2", bg = 'orange', fg = 'green')
button_3 = Button(top_frame, text = "button_3", bg = 'black', fg = 'yellow')
button_4 = Button(bottom_frame, text = "button_4", bg = 'green', fg = 'blue')

button_1.pack(side = LEFT)
button_2.pack(side = LEFT)
button_3.pack(side = LEFT)
button_4.pack(side = BOTTOM)

root.mainloop()