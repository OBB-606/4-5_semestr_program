import pytest
from tkinter import *
"События мыши"

def left_click(event):
    frame_1.configure(bg = 'yellow')
    frame_3.configure(bg = 'white')
    frame_2.configure(bg = 'white')

def middle_click(event):
    frame_2.configure(bg = 'yellow')
    frame_3.configure(bg = 'white')
    frame_1.configure(bg = 'white')

def right_click(event):
    frame_3.configure(bg = 'yellow')
    frame_1.configure(bg = 'white')
    frame_2.configure(bg = 'white')


root = Tk()

root.configure(bg = 'red')

frame_1 = Frame(root, width = 250, height = 250, bg = 'white')
frame_2 = Frame(root, width = 250, height = 250, bg = 'white')
frame_3 = Frame(root, width = 250, height = 250, bg = 'white')

frame_1.grid(row = 0, column = 0)
frame_2.grid(row = 0, column = 1, padx = 1)#padx делает отступ по иксу
frame_3.grid(row = 0, column = 2)

root.bind("<Button-1>", left_click)
root.bind("<Button-2>", middle_click)
root.bind("<Button-3>", right_click)

root.mainloop()
