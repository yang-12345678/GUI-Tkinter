# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("ch2_1")
root.geometry("300x160")  # 窗口大小
# label = ch1_Label(root, text="I like tkinter")
# label.pack()  # 包装与定位组件
# ch1_Label(root, text="I like tkinter").pack()
label = Label(root, text="I like tkinter").pack()
# 与第一种传回的数据类型不同，对此对象进一步操作 Widget 控件就会报错
# 建议pack与label 分开，不需要进一步操作时才合在一起
print(type(label))

# 默认大小会比没有控件时更小，因为Tkinter只会安排足够的空间显示控件
root.mainloop()
