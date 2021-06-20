# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("ch2_2")

# Widget的共同属性：font:设置字体  Helvetic字体，20大小，粗体显示
label = Label(root, text="ancdefghijklmnopqrstuvwxyz", fg="blue", bg="yellow",
              height=3, width=30,
              font=("Source Code Pro", 20, "bold"))  # font=("Helvetic 20 bold")
label.pack()

# 第二个容器
root1 = Tk()
root1.title("test")
# justify: 最后一行靠左对齐，默认居中
label1 = Label(root1, text="ancdefghijklmnopqrstuvwxyz",
               fg="blue", bg="lightyellow",
               height=3, width=15,
               wraplength=80,
               justify="left"  # 最后一行靠左对齐
               )
label1.pack()

root.mainloop()
