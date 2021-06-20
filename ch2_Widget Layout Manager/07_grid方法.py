# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("test")

lab1 = Label(root, text="安徽理工大学",
             bg="lightyellow",
             width=15)
lab2 = Label(root, text="中国科学技术大学",
             bg="lightgreen",
             width=15)
lab3 = Label(root, text="安徽大学",
             bg="lightblue",
             width=15)

# 类似与 一种 Excel 表格形式
lab1.grid(row=0, column=0)
lab2.grid(row=1, column=0)
lab3.grid(row=1, column=1)

root.mainloop()
