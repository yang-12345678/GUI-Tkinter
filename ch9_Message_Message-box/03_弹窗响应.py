# -*- coding: utf-8 -*-
# Date: 2021/06/16

from tkinter import *
from tkinter import messagebox


def myMsg1():
    ret = messagebox.askokcancel("test1", "安装失败，再试一次？")
    print("安装失败", ret)


def myMsg2():
    ret = messagebox.askyesnocancel("test2", "编辑完成，是或否或取消？")
    print("编辑完成", ret)


root = Tk()
root.title("test")

Button(root, text="安装失败", command=myMsg1).pack()
Button(root, text="安装完成", command=myMsg2).pack()

root.mainloop()