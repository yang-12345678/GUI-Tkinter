# -*- coding: utf-8 -*-
# Date: 2021/06/14
from tkinter import *

root = Tk()
root.title("ch8_5")
fm = Frame(width=150, height=80, relief=RAISED, borderwidth=5)  # 创建框架
lab = Label(fm, text="请复选常用的程序语言")
# 创建标签
lab.pack()
python = Checkbutton(fm, text="Python")
# 创建Phthon复选框
python.pack(anchor=W)
java = Checkbutton(fm, text="Java")
# 创建Java复选框
java.pack(anchor=W)
ruby = Checkbutton(fm, text="Ruby")
# 创建Ruby复选框
ruby.pack(anchor=W)
fm.pack(padx=10, pady=10)
# 包装框架
root.mainloop()
