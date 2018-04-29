# conda_python3_code

from tkinter import *

def callback():
    print (u"你好~")
def popup(event):
    menubar.post(event.x_root,event.y_root)

root = Tk()

menubar=Menu(root)
menubar.add_command(label="撤销",command=callback)
menubar.add_command(label="重做",command=root.quit)

frame=Frame(root,width=300,height=300)
frame.pack()
# MAC is button-2 to define the right-click
frame.bind("<Button-2>",popup)

mainloop()