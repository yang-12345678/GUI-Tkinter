# -*- coding: utf-8 -*-
# Date: 2021/06/12

from tkinter import *

'''
个人理解：
传入参数中有 mode 模式，比如调用callbackW():
就会传入模式W, 此时R模式将不能被执行，所以xE.get()不会触发callbackR()
'''
def callbackW(*args):
    xL.set(xE.get())
    print("执行更改追踪")



def callbackR(*args):
    print("warning:数据被读取！")


def hit():
    print("读取数据：", xE.get())
    xE.set("*****")


root = Tk()
root.title("test")

xE = StringVar()

entry = Entry(root, textvariable=xE)
entry.pack(pady=5, padx=10)
xE.trace("w", callbackW)
xE.trace("r", callbackR)
# xE.get()
# x()


xL = StringVar()
label = Label(root, textvariable=xL)
xL.set("同步显示")
label.pack(pady=5, padx=10)
xE.set("你好")
xE.set("你好")
xE.set("====")
btn = Button(root, text="读取", command=hit)
btn.pack(pady=5)
root.mainloop()
