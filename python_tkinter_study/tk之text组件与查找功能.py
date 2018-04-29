# conda_python3_code

from tkinter import *

def getIndex(text,index):
    return tuple(map(int,str.split(text.index(index),'.')))
root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,'Chingchi__All right reserved')
start = '1.0'
while True:
    pos = text.search('i',start,stopindex=END)
    if not pos:
        break
    print('Found it ! It is in ',getIndex(text,pos))
    start = pos + '+1c'

mainloop()