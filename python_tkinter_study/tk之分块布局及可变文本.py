# conda_python3_code

from tkinter import *
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

def callback():
    var.set('Thank you ! \n'
            'hope to see you again ! ')

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('Welcome to Guangzhou\n'
        'CBD,Zhujiang new city')

textLabel = Label(frame1,textvariable=var,justify=LEFT,padx=10,bg='black',fg='white',font=('Bradley Hand',20))
textLabel.pack(side=TOP,fill=X)

img = Image.open('Guangzhou.jpg')  # open and decode image
photo = ImageTk.PhotoImage(img)
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side=BOTTOM)

the_button = Button(frame2,text='Click item : I love Guangzhou ! ',fg='black',bg='white',font=('Bradley Hand',20),command=callback)
the_button.pack(side = LEFT,padx=10,pady=10)
the_button = Button(frame2,text='Exit ! ',fg='black',bg='white',font=('Bradley Hand',20),command=exit)
the_button.pack(side = RIGHT,padx=10,pady=10)

frame1.pack(padx=10,pady=10,side=TOP)
frame2.pack(padx=10,pady=10,side=BOTTOM)

mainloop()