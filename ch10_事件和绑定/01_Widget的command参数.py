# -*- coding: utf-8 -*-
# Date: 2021/06/16

from tkinter import *


def python_clicked():

    if varPython.get():
        lab.config(text="Select Python")

def java_clicked():
    if varJava.get():
        lab.config(text="Select Java")


def button_clicked():
    lab.config(text="Button clicked")


root = Tk()
root.title("test")
root.geometry("300x180")

btn = Button(root, text="Click me", command=button_clicked)
btn.pack(anchor=W)
varPython = BooleanVar()
cbnPython = Checkbutton(root, text="Python", variable=varPython,
                        command=python_clicked)
cbnPython.pack(anchor=W)

varJava = BooleanVar()
cbnJava = Checkbutton(root, text="Java", variable=varJava,
                        command=java_clicked)
cbnJava.pack(anchor=W)

lab = Label(root, bg="yellow", fg="blue",
            height=2, width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()
