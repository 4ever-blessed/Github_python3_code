# conda_python3_code

from tkinter import *
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

# root = Tk()
#
# v = IntVar()
# Radiobutton(root,text='C',variable=v,value=1).pack(anchor=W,padx=20,pady=5)
# Radiobutton(root,text='Java',variable=v,value=2).pack(anchor=W,padx=20,pady=5)
# Radiobutton(root,text='Python',variable=v,value=3).pack(anchor=W,padx=20,pady=5)
# Radiobutton(root,text='Ruby',variable=v,value=4).pack(anchor=W,padx=20,pady=5)
# # When the value is different , it will be mutex
#
# mainloop()


# for_loop method
# indicatoron = False means the presentation of selected or unselected
root = Tk()

group = LabelFrame(root,text='Which is the best language ? ',padx=5,pady=5)
group.pack(padx=10,pady=10)
Langs = [('C',1),('Java',2),('Python',3),('Ruby',4)]
v = IntVar()
v.set(1)
for lang,num in Langs:
    b = Radiobutton(group,variable=v,text=lang,value=num,indicatoron=True)
    b.pack(fill=X)

mainloop()
