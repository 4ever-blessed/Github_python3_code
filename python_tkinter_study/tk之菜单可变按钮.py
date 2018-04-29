# conda_python3_code

from tkinter import *

root = Tk()

variable = StringVar()
variable.set("one")

w = OptionMenu(root,variable,"one","two","three")
w.pack()

mainloop()