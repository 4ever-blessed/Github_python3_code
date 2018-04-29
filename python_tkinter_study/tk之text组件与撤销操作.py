# conda_python3_code

from tkinter import *

def show():
    text.edit_undo()
root = Tk()

text = Text(root,width=30,height=5,undo=True)
text.pack()

text.insert(INSERT,'Chingchi__All right reserved')

Button(root,text='UNDO',command=show).pack()

mainloop()