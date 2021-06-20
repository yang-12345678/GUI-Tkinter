# -*- coding: utf-8 -*-
# Date: 2021/06/14

from tkinter import *

window = Tk()
window.title("test")

slider1 = Scale(window, from_=0, to=10).pack()
slider2 = Scale(window, from_=0, to=10,
                length=300, orient=HORIZONTAL).pack()
window.mainloop()
