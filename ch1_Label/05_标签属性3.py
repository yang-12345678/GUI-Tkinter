# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

root = Tk()
root.title("test")

# bitmap: 在标签位置放置内建位图
# compound: 定义文字与图像的位置关系（两者共存时）
label = Label(root, bitmap="hourglass",
              compound="right", text='我的天空')  # 图像在右边
label.pack()

root.mainloop()
