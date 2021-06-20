# -*- coding: utf-8 -*-
# Date: 2021/06/11

from tkinter import *


def btn_hit():
    global msg_on
    if msg_on == False:
        msg_on = True
        x.set("I Like tkinter")
    else:
        msg_on = False
        x.set("")


root = Tk()
root.title("title")

msg_on = False
x = StringVar()  #  Label的变量内容

label = Label(root, textvariable=x,
              fg="blue", bg="lightyellow",
              font="Verdana 16 bold",
              width=25, height=2)

label.pack()

btn = Button(root, text="Click Me", command=btn_hit)
btn.pack()

root.mainloop()
