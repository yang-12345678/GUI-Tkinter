# -*- coding: utf-8 -*-
# Date: 2021/06/17

from tkinter import *

root = Tk()
root.title("test")
root.geometry("300x180")

var = StringVar(root)
optionmenu = OptionMenu(root, var, "python","java", "c#")
optionmenu.pack()

root.mainloop()