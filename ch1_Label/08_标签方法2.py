# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

counter = 0  # 计数的全局变量


# Widget的共同方法：config()
def run_counter(digit):
    """数字内容的更新"""

    def counting():  # 更新数字的方法
        global counter
        counter += 1
        # Widget控件在建立时可以直接设置对象属性
        # 若是部分属性未建立，未来在程序执行时如果想要建立或是更改属性可以使用config()方法
        # 此方法内属性设置的参数用法与建立时相同
        digit.config(text=str(counter))
        # 每个 1000ms 会调用第二个参数的方法
        digit.after(1000, counting)

    counting()


root = Tk()
root.title("test")

digit = Label(root, bg="yellow", fg="blue",
              height=3, width=10,
              font="Helvetic 20 bold")
digit.pack()
run_counter(digit)
root.mainloop()
