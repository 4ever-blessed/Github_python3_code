# conda_python3_code

from tkinter import *

root = Tk()

def callback():
    print (u"你好~")

# relief is to set the style of menubutton
mb = Menubutton(root,text="点我",relief=RAISED)
mb.pack()

filemenu = Menu(mb,tearoff=False)
filemenu.add_command(label="打开",command=callback)
filemenu.add_command(label="保存",command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出",command=root.quit)

mb.config(menu=filemenu)

mainloop()