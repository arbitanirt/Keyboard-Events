import tkinter as tk
from tkinter import *



mainwindow = tk.Tk()
mainwindow.title("Move objects by Mouse")

current_wid_pos_x= None
current_wid_pos_y= None

def object_picked_up(event):
    global current_wid_pos_x, current_wid_pos_y

    current_wid_pos_x = event.x
    current_wid_pos_y = event.y

    wid = event.widget
    #print('object_picked_up : ', event)

def object_moving(event):
    global current_wid_pos_x, current_wid_pos_y

    wid = event.widget

    x = wid.winfo_x() - current_wid_pos_x + event.x
    y = wid.winfo_y() - current_wid_pos_y + event.y

    wid.place(x=x, y=y)

    #print('object_moving : ', event)

l1 = Label(mainwindow)
l1.config(bg="green")
l1.place(x=10, y=10,width=100, height=100)
mainwindow.bind("<Button-1>", object_picked_up)
mainwindow.bind("<B1-Motion>", object_moving)


l2 = Label(mainwindow)
l2.config(bg="red")
l2.place(x=200, y=10,width=100, height=100)

l2.bind("<Button-1>", object_picked_up)
l2.bind("<B1-Motion>", object_moving)


b1 = Button(mainwindow)
b1.place(x=100, y=300,width=100, height=100)




mainwindow.config(padx=10, pady=10, bg='yellow')
mainwindow.geometry("500x500")
mainwindow.mainloop()