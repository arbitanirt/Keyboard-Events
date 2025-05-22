import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title('Move Objects by Keyboard keys')

def right_key_handler(event):
    l1.place(x=l1.winfo_x()+8, y=l1.winfo_y())

def left_key_handler(event):
    l1.place(x=l1.winfo_x()-8, y=l1.winfo_y())

def up_key_handler(event):
    l1.place(x=l1.winfo_x(), y=l1.winfo_y()-8)

def down_key_handler(event):
    l1.place(x=l1.winfo_x(), y=l1.winfo_y()+8)

l1 = Label(mainwindow, bg='blue')
l1.place(x=10, y=10, width=100, height=100)


mainwindow.bind('<Right>', right_key_handler)
mainwindow.bind('<Left>', left_key_handler)
mainwindow.bind('<Up>', up_key_handler)
mainwindow.bind('<Down>', down_key_handler)







mainwindow.geometry('500x500')
mainwindow.mainloop()