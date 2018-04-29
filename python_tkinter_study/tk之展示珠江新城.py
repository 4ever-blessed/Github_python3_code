# conda_python3_code

from tkinter import *
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

root = Tk()

textLabel = Label(root,text='Welcome to Guangzhou\n'
                            'CBD,Zhujiang new city',justify=LEFT,padx=10,bg='black',fg='white',font=('Bradley Hand',20))
textLabel.pack(side=TOP)

img = Image.open('Guangzhou.jpg')  # open and decode image
photo = ImageTk.PhotoImage(img)
imgLabel = Label(root,image=photo)
imgLabel.pack(side=BOTTOM)

mainloop()