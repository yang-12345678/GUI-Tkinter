# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("test")

# Widget的共同属性： relief: 外框
# padx/y:标签文字与标签区间的间距：上下间距 10，左右间距 5
label = Label(root, text="raised", relief="raised",
              bg="lightgreen", padx=5, pady=10)
label.pack()

root1 = Tk()
# Widget的共同属性：cursor:可以设置光标在 标签 或者 按钮 上时的形状
# 默认同 父容器上的形状
label = Label(root1, text='raised', relief='raised',
              bg="lightyellow",
              padx=5, pady=10,
              cursor="heart")  # 心形
label.pack()

root.mainloop()
