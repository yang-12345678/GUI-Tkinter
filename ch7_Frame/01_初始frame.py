# -*- coding: utf-8 -*-
# Date: 2021/06/14

from tkinter import *
# root = Tk()
# root.title("test")
#
# for fm in ['red', 'green', 'blue']:
#     Frame(root, bg=fm, height=50, width=250).pack()

root = Tk()
root.title("test")

fms = {'red': 'cross', 'green': 'boat', 'blue': 'clock' }

for fmColor in fms:
    Frame(root, bg=fmColor, cursor=fms[fmColor],
          height=50, width=200).pack(side=LEFT)



root.mainloop()