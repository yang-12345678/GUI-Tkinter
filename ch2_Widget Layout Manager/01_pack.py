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
'''
side参数的不同选择：
1. TOP：默认值, 从上往下排列
2. BOTTOM：从下往上排列
3. LEFT：从左往右排列
4. RIGHT：从右往左排列
'''
# lab1.pack(side=LEFT)
# lab2.pack(side=LEFT)
# lab3.pack(side=LEFT)

# 混合使用
lab1.pack()
lab2.pack(side=RIGHT)
lab3.pack(side=LEFT)

window.mainloop()
