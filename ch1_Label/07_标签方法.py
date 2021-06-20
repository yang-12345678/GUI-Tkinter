# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("test")
root.geometry("1920x1080")

# 显示 jpg 的方法
image = Image.open("123.jpg")
# image = PhotoImage(file="123.jpg")   # 仅支持 png,gif
img = ImageTk.PhotoImage(image)
label = Label(root, image=img)
label.pack()

root.mainloop()