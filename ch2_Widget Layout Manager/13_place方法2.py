# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("test")
root.geometry("640x180")

image = Image.open("123.jpg")
img = ImageTk.PhotoImage(image)
lab1 = Label(root, image=img)
# relwidth/relheight: 相对于容器的位置
lab1.place(x=20, y=30, width=200, height=120)
root.mainloop()
