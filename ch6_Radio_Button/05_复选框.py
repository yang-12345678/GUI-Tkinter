# -*- coding: utf-8 -*-
# Date: 2021/06/14

from tkinter import *

def printInfo():
    print(var1.get())
    print(var2.get())

root = Tk()
root.title("test")

lab = Label(root, text="请选择喜欢的活动", fg="blue", bg="lightyellow", width=30)
lab.grid(row=0)

var1 = IntVar()
cbtnNFL = Checkbutton(root, text="美式足球", variable=var1)
cbtnNFL.grid(row=1, sticky=W)

var2 = IntVar()

cbtnMLB = Checkbutton(root, text="棒球", variable=var2)
cbtnMLB.grid(row=2, sticky=W)

var3 = IntVar()
cbtnNBA = Checkbutton(root, text="篮球", variable=var3)
cbtnNBA.grid(row=3, sticky=W)

btn = Button(root, text="确定", width=10, command=printInfo)
btn.grid(row=4)

root.mainloop()