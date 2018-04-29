# conda_python3_code

from tkinter import *
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

root = Tk()
img = Image.open('Guangzhou.jpg')  # open and decode image
photo = ImageTk.PhotoImage(img)
imgLabel = Label(root,image=photo,
                 text='Welcome to Guangzhou ! \n'
                            'CBD,Zhujiang new city ! ',
                 justify=LEFT,padx=10,fg='white',compound=CENTER,font=('Comic Sans MS',20))
imgLabel.pack()

mainloop()