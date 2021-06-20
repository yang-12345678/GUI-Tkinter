# -*- coding: utf-8 -*-
# Date: 2021/06/14
from tkinter import *

root = Tk()
root.title("ch8_7")


labFrame = LabelFrame(root, text="数据验证")  # 创建框架标签
accountL = Label(labFrame, text="Account")  # account标签
accountL.grid(row=0, column=0)
pwdL = Label(labFrame, text="Password")
# pwd标签
pwdL.grid(row=1, column=0)
accountE = Entry(labFrame)
# account文本框
accountE.grid(row=0, column=1)
# 定位account文本框
pwdE = Entry(labFrame, show="*")
# pwd文本框
pwdE.grid(row=1, column=1, pady=10)
# 定位pwd文本框
labFrame.pack(padx=10, pady=5, ipadx=5, ipady=5)  # 包装与定位标签框架
root.mainloop()
