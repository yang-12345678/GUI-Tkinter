# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("test")

myTitle = "一个人的极境旅行"
myContent = """2016年12月，我一个人订了机票和船票，
开始我的南极旅行，飞机经迪拜再往阿根廷的乌斯怀亚，
在此我登上了邮轮开始我的南极之旅"""

lab1 = Label(root,text=myTitle,font="Helvetic 20 bold")
lab1.pack(padx=10,pady=10)

sep = Separator(root,orient=HORIZONTAL) # 水平线和竖直线
sep.pack(fill=X,padx=5)  # 与窗口边界左右均相距 5 像素

lab2 = Label(root,text=myContent)
lab2.pack(padx=10,pady=10)

root.mainloop()
