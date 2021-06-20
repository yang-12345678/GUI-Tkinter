# -*- coding: utf-8 -*-
# Date: 2021/06/15
from tkinter import *


def printInfo():
    print("垂直尺度值= %d，水平尺度值=%d" % (sv.get(), sH.get()))
root = Tk()
root.title("ch9_3")
# 窗口标题
sv = Scale(root, label="垂直", from_=0, to=20)

# 建立垂直尺度
sv.set(5)
# 设定垂直尺度初值是5
sv.pack()
sH = Scale(root, label="水平", from_=0, to=10,  # 建立水平尺度
           length=300, orient=HORIZONTAL)
sH.set(3)
# 设定水平尺度初值是3
sH.pack()
Button(root, text="Print", command=printInfo).pack()
root.mainloop()

