# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("test")
# 设置缩放比
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

lab1 = Label(root, text="ch1_Label 1", bg="pink")
lab1.grid(row=0, column=0, padx=5, pady=5)

lab2 = Label(root, text="ch1_Label 2", bg="lightblue")
lab2.grid(row=0, column=1, padx=5, pady=5)

lab3 = Label(root, bg="yellow")
lab3.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
