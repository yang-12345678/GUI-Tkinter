# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("test")

label = Label(root, text="I like tkinter")
label.pack()
# 用列表形式传回这个 Widget 所有的参数
print(label.keys())

root.mainloop()