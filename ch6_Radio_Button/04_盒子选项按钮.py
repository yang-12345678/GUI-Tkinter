# -*- coding: utf-8 -*-
# Date: 2021/06/13

from tkinter import *


def printSelection():
    print(cities[var.get()])


root = Tk()
root.title("test")

cities = {0: "东京", 1: "纽约", 2: "巴黎", 3: "伦敦", 4: "香港"}

var = IntVar()
var.set(0)
label = Label(root, text="选择你最喜欢的城市",
              fg="blue", bg="lightyellow", width=30).pack()

for val, city in cities.items():
    Radiobutton(root,
                text=city,
                indicatoron=0,  # 盒子取代选项按钮
                width=30,
                variable=var, value=val,
                command=printSelection).pack()

root.mainloop()
