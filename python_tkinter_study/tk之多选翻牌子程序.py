# conda_python3_code

from tkinter import *
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

root =Tk()

Code_language = ['C','Java','Python','Ruby']

v = []

for code_language in Code_language:
    v.append(IntVar())
    b = Checkbutton(root,text=code_language,variable=v[-1])
    b.pack(anchor=W,padx=30,pady=5) # set left justifying

mainloop()