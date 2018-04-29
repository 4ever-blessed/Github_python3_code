# conda_python3_code

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format


def show():
    # insert the image
    text.image_create(END,image=photo)

root = Tk()

img = Image.open('calc.jpg')
photo = ImageTk.PhotoImage(img)

text = Text(root,width=30,height=20)
text.pack()

text.insert(INSERT,'Chingchi\n')
text.insert(END,'All right reserved')

b1 = Button(text,text='Insert image',command=show)
text.window_create(INSERT,window=b1)


mainloop()