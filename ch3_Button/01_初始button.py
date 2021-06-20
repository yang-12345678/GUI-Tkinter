# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *


def msgShow():
    label['text'] = "I love Python"
    label['bg'] = "lightyellow"
    label['fg'] = 'blue'


root = Tk()
root.title("test")
root.geometry("300x180")
label = Label(root)
btn = Button(root, text="打印消息", command=msgShow)
label.pack()
btn.pack()

root.mainloop()
