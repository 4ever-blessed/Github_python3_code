# conda_python3_code

from tkinter import *

# message is the advanced func of label
# it can be change the row automatically

root = Tk()

w1 = Message(root,text="这是一则消息",width=100)
w1.pack()

w2 = Message(root,text="这是一则骇人听闻的长长长长长长消息！",width=100)
w2.pack()

mainloop()