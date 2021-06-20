# -*- coding: utf-8 -*-
# Date: 2021/06/16

from tkinter import *

root = Tk()
root.title("test")

myText = "人生若只如初见，何事秋风悲画扇"
msg = Message(root, bg="yellow", text=myText, font="times 12 italic")
msg.pack(padx=10, pady=10)

root.mainloop()