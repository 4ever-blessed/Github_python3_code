# conda_python3_code

from tkinter import colorchooser
from tkinter import *

root = Tk()

def callback():
    fileName = colorchooser.askcolor()
    print(fileName)

Button(root,text="选择颜色",command=callback).pack()

mainloop()