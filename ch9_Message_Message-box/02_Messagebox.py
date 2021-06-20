# -*- coding: utf-8 -*-
# Date: 2021/06/16

from tkinter import *
from tkinter import messagebox


def myMsg():
    # 标题，内容，选项
    messagebox.showinfo("My Message Box", "Python Tkinter早安")


window = Tk()
window.title("test")
window.geometry("300x160")

btn = Button(window, text="Good Morning", command=myMsg).pack()

window.mainloop()
