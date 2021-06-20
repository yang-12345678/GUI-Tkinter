# -*- coding: utf-8 -*-
# Date: 2021/06/14
from tkinter import *
import random

root = Tk()
root.title("ch8_11")
msgYes, msgNo, msgExit = 1, 2, 3


def MessageBox():
    # 创建对话框
    msgType = random.randint(1, 3)
    # 随机数产生对话框方式
    if msgType == msgYes:
        # 产生Yes字符串
        labTxt = 'Yes '
    elif msgType == msgNo:
        # 产生No字符串
        labTxt = 'No'
    elif msgType == msgExit:
        # 产生Exit字符串
        labTxt = 'Exit'

    tl = Toplevel()
    # 建立Toplevel窗口
    tl.geometry("300x180")
    # 设置对话框大小
    tl.title("Message Box")
    Label(tl, text=labTxt).pack(fill=BOTH, expand=True)


btn = Button(root, text='Click Me ', command=MessageBox)
btn.pack()
root.mainloop()
