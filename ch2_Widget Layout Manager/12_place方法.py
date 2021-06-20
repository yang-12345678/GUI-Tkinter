# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

# place 可以直接设定标签的位置
window = Tk()
window.title("ch3_36")
lab1 = Label(window, text="明志科技大学",
             bg="lightyellow",
             width=15)
lab2 = Label(window, text="长庚大学",
             bg="lightgreen",
             width=15)
lab3 = Label(window, text="长庚科技大学",
             bg="lightblue",
             width=15)
lab1.place(x=0, y=0)
lab2.place(x=30, y=50)
lab3.place(x=60, y=100)
window.mainloop()
