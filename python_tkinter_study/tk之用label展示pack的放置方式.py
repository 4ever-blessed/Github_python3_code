# conda_python3_code

from tkinter import *

root = Tk()

Label(root,text="red",bg="red",fg="white").pack(fill=X)
Label(root,text="green",bg="green",fg="black").pack(fill=X)
Label(root,text="blue",bg="blue",fg="white").pack(fill=X)

Label(root,text="red",bg="red",fg="white").pack(side=LEFT)
Label(root,text="green",bg="green",fg="black").pack(side=RIGHT)
Label(root,text="blue",bg="blue",fg="white").pack(side=LEFT)

mainloop()