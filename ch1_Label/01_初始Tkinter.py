# -*- coding: utf-8 -*-v
# date: 2021/05/31

from tkinter import *

root = Tk()  # 根窗口，也称为 容器

root.title("mywindow") # 窗口标题
root.geometry("300x160") # 窗口大小
root.configure(bg='yellow') # 窗口背景颜色
# root.configure(bg='#00ff00') # 窗口背景颜色,另一种方式

#root.iconbitmap("mystar.ico")
root.mainloop()  # 事件循环，程序继续执行，等待与处理窗口事件，放在最后一行
