from tkinter import *
"Метод bind()"

def output(event):
    txt = entry_1.get()

    try:
        if int(txt) < 18:
            label_1["text"] = "fuck you!"
        else:
            label_1["text"] = "GO GO!"
        entry_1.delete(0, END)
    except :
        label_1['text'] = "fuck you, asshole!"
        entry_1.delete(0, END)


root = Tk()
root.title("How you old?")
entry_1 = Entry(root, width = 3, font = 15)
#              окно   ширина     размер шрифта
button_1 = Button(root, text = "Check")
label_1  = Label(root, width = 27, font = 15)

entry_1.grid(row = 0, column = 0)
button_1.grid(row = 0, column = 1)
label_1.grid(row = 0, column = 2)

button_1.bind("<Button-1>", output)

root.mainloop()