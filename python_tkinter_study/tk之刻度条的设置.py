# conda_python3_code

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format
def show():
    print('Lv is ',s2.get(),', Ability is ',s1.get())

master = Tk()
# tickinterval means the interval of display number
# resolution means the unit of number
s1 = Scale(master,from_=0,to=21,tickinterval=5,resolution=0.1,length=200)
s1.pack()
s2 = Scale(master,from_=0,to=129,orient=HORIZONTAL,tickinterval=10,resolution=1,length=600)
s2.pack()
Button(master,text='Get state',command=show).pack()

mainloop()