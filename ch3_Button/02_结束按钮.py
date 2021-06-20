# -*- coding: utf-8 -*-
# Date: 2021/06/05

from tkinter import *


def msgShow():
    label.config(text="I Love Python", bg="lightyellow", fg="blue")


root = Tk()
root.title("test")
label = Label(root)

btn1 = Button(root, text="打印消息", width=15, command=msgShow)
btn2 = Button(root, text="结束", width=15, command=root.quit)
label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
root.mainloop()

