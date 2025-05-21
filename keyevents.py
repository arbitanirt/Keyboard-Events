import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title('KeyEvents')

#def key_handler(event):
#    print('w is pressed!')

#def A_key_handler(event):
#    print('a is pressed!')

#def key_handler(event):
#    print('w is pressed!')

def key_handler(event):
    print('key pressed is: ', event.keysym)
    l1.config(text=event.keysym)

    if event.keysym == 'a':
        print('A is Pressed')
        l1.config(text='A is pressed')

#mainwindow.bind('<w>', key_handler)
#mainwindow.bind('<a>', A_key_handler)
mainwindow.bind('<Key>', key_handler)

l1 = Label(mainwindow, height=5, width=10, relief='groove', bd=5, font=(None, 40))
l1.pack()




mainwindow.geometry('500x500')
mainwindow.mainloop()