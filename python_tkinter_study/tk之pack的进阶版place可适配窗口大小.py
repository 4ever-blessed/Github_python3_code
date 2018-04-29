# conda_python3_code

from tkinter import *
from PIL import Image,ImageTk

def callback():
    print ("正中靶心！")

root = Tk()

img = Image.open('Guangzhou.jpg')  # open and decode image
photo = ImageTk.PhotoImage(img)
Label(root,image=photo).place(relx=0.5,rely=0.5,
                                              relheight=0.8,relwidth=0.8,anchor=CENTER)
Button(root,text="点我",command=callback).place(relx=0.5,rely=0.5,
                                              relheight=0.5,relwidth=0.5,anchor=CENTER)

mainloop()