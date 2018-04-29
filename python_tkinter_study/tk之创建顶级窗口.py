# conda_python3_code

from tkinter import *

root = Tk()

def create():
    top = Toplevel()
    top.attributes("-alpha",0.8)
    top.title("FishC Demo")

    msg = Message(top,text="This is the message in the toplevel")
    msg.pack()

Button(root,text="创建顶级窗口",command=create).pack()

mainloop()