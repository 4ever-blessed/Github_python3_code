# conda_python3_code

from tkinter import *

# spinbox is the another func of listbox

root = Tk()

#w = Spinbox(root,from_=0,to=10)
w = Spinbox(root,values=("Python","C","Java","Ruby"))
w.pack()

mainloop()