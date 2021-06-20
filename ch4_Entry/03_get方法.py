# -*- coding: utf-8 -*-
# Date: 2021/06/05

from tkinter import *

def printInfo():
    print(f"Account:{accountE.get()}\nPassword:{pwdE.get()}")

root = Tk()
root.title("test")

accountL = Label(root, text="Account")
accountL.grid(row=0)
pwdL = Label(root, text="Password")
pwdL.grid(row=1)

accountE = Entry(root)
pwdE = Entry(root, show="*")
accountE.grid(row=0, column=1)
pwdE.grid(row=1, column=1)

loginbtn = Button(root, text="Login", command=printInfo)
quitbtn = Button(root, text="Quit", command=root.quit)
loginbtn.grid(row=2, column=0, sticky=W, pady=5)
quitbtn.grid(row=2, column=1, sticky=W, pady=5)

root.mainloop()
