# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("ch2_2")
# fg: 前景色  bg: 背景色
# height: 3  width: 15
# anchor: 标签文字在标签区域输出位置的设置，默认居中对齐 nw:左上角 se:右下角
# wraplength: 设置标签中文字在多少像素宽度后自动换行
label = Label(root, text="I like Tkinter", fg="blue", bg="yellow",
              height=3, width=15,anchor="nw",
              wraplength=40)  # anchor=NW 大写内部为常量，不用引号
label.pack()

root.mainloop()
