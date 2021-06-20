# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("test")
root.geometry("300x180")

okLabel = Label(root, text='OK',
                font="Times 20 bold",
                fg="white", bg="blue")
# anchor: 控件内容在控件区域输出位置的设置
okLabel.pack(anchor=S, side=RIGHT, padx=10, pady=10)  # Ｓ 是下方，从右边开始排

noLabel = Label(root, text="NO",
                font="Times 20 bold",
                fg="white", bg="red")
noLabel.pack(anchor=S, side=RIGHT, pady=10)

root.mainloop()
