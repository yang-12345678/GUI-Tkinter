# -*- coding: utf-8 -*-
# Date: 2021/06/05

from tkinter import *

root = Tk()
root.title("test")

nameL = Label(root, text="Name ")
nameL.grid(row=0)  # 没有设置 column 的情况下，自动设置为0
addressL = Label(root, text="Address")
addressL.grid(row=1)

nameE = Entry(root)
addressE = Entry(root)
nameE.grid(row=0,column=1)
addressE.grid(row=1, column=1)

root.mainloop()