# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

window = Tk()
window.title("test")

lab1 = Label(window, text="安徽理工大学",
             bg="lightyellow",
             width=15)  # 浅黄色
lab2 = Label(window, text="中国科学技术大学",
             bg="lightgreen",
             width=15)  # 浅绿色
lab3 = Label(window, text="合肥工业大学",
             bg="lightblue",
             width=15)  # 浅蓝色

# lab1.pack(fill=X, pady=10)
# lab2.pack(pady=10)
# lab3.pack(fill=X)

# padx/y: 控件和窗口或控件与控件之间的距离
# ipadx/y: 控制标签文字和标签容器的间距
lab1.pack(side=LEFT)
lab2.pack(side=LEFT, padx=50)
lab3.pack(side=LEFT)

window.mainloop()
