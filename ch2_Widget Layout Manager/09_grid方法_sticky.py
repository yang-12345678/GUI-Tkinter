# -*- coding: utf-8 -*-
# Date: 2021/06/01

from tkinter import *

window = Tk()
window.title("test")
lab1 = Label(window, text="安徽理工大学",relief="raised")
lab2 = Label(window, bg="yellow", width=20,relief="raised")
lab3 = Label(window, text="中国科学技术大学",relief="raised")
lab4 = Label(window, bg="aqua", width=20,relief="raised")
lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W+E)
lab2.grid(row=0, column=1, padx=5, pady=5)
lab3.grid(row=1, column=0, padx=5)
lab4.grid(row=1, column=1, padx=5)

window.mainloop()