# -*- coding: utf-8 -*-
# Date: 2021/06/16

from tkinter import *

def callback(event):
    print("Clicked", event.x, event.y)


root = Tk()
root.title("test")

frame = Frame(root, width=300, height=180)
root.bind("<Button-1>", callback)
frame.pack()

root.mainloop()