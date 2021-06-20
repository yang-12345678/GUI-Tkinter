# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

window = Tk()
window.title("test")
lab1 = Label(window, text="安徽理工大学", bg="lightyellow")
lab2 = Label(window, text="中学科学技术大学", bg="lightgreen")
lab3 = Label(window, text="安徽大学", bg="lightblue")
# fill: 设置控件填满所分配容器区间的方式，
# lab1.pack(fill=X)
# lab2.pack(fill=Y)  # 已经占满其分配空间的Y轴，不会其任何作用
# lab3.pack(fill=X)

lab1.pack(side=LEFT, fill=Y)
lab2.pack(fill=X)
# 没有expand不能成功， 原因在书上
lab3.pack(fill=BOTH,expand=True)

window.mainloop()
