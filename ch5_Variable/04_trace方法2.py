# -*- coding: utf-8 -*-
# Date: 2021/06/12

from tkinter import *


def callback(*args):
    xL.set(xE.get())

    print("data changed:", xE.get())


root = Tk()
root.title("test")

xE = StringVar()
entry = Entry(root, textvariable=xE)
entry.pack(pady=5, padx=10)
xE.trace("w", callback)

xL = StringVar()
label = Label(root, textvariable=xL)
xL.set("同步显示")
label.pack(pady=5, padx=10)

root.mainloop()
