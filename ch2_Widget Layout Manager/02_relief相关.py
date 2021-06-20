# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

relief = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']

window = Tk()
window.title("test")

for Relief in relief:
    Label(window, text=Relief, relief=Relief,
          fg="blue",
          font="Times 20 bold").pack(side=LEFT, padx=5)

window.mainloop()