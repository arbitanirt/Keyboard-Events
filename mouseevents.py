import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title("MouseEvents")

def mouse_event_handler(event):
    #print('event : ', event)
    #l1.config(text='Mouse event received')
    l1.config(text=str(event.x) + " " + str(event.y))

#mainwindow.bind('<Button-1>', mouse_event_handler)
#mainwindow.bind('<Button-3>', mouse_event_handler)
#mainwindow.bind('<ButtonRelease>', mouse_event_handler)
#mainwindow.bind('<Enter>', mouse_event_handler)
#mainwindow.bind('<Leave>', mouse_event_handler)
mainwindow.bind('<Motion>', mouse_event_handler)



l1 = Label(mainwindow, height=8, width=16, relief='groove', bd=5, font=(None, 30), wraplength=200)
l1.pack()



mainwindow.geometry("500x500")
mainwindow.mainloop()