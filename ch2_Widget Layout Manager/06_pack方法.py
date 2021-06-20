# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("test")
root.geometry("300x180")
# 传回所有 Widget 控件对象
print("执行前：", root.pack_slaves())
oklabel = Label(root, text="OK", font="Times 20 bold",
                fg="white", bg="blue")

oklabel.pack(anchor=S, side=RIGHT,
             padx=10,pady=10)
nolabel = Label(root, text="NO", font="Times 20 bold",
                fg="white", bg="red")
nolabel.pack(anchor=S, side=RIGHT,
             pady=10)
print("执行后：", root.pack_slaves())

root.mainloop()
