# conda_python3_code

from tkinter import *
import hashlib

def getSig(contents):
    s = hashlib.md5(contents.encode())
    return s.digest()
def check():
    contents = text.get('1.0',END)
    if sig != getSig(contents):
        print('The content has been changed ! ')
    else:
        print('The result is OK ! ')
root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,'Chingchi__All right reserved')
contents = text.get('1.0',END)
sig = getSig(contents)
Button(root,text='check',command=check).pack()

mainloop()