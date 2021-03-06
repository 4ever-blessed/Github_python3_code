# conda_python3_code

from tkinter import *
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

# Clear text display

# def show():
#     print('Your name is %s'% e1.get())
#     print('Your id is %s'% e2.get())
# root = Tk()
#
# Label(root,text='name:').grid(row=0,column=0)
# Label(root,text='ID:').grid(row=1,column=0)
#
# e1 = Entry(root)
# e2 = Entry(root)
# e1.grid(row=0,column=1,padx=5,pady=5)
# e2.grid(row=1,column=1,padx=5,pady=5)
#
# Button(root,text='Confirm',width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
# Button(root, text='Exit', width=10, command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)
#
# mainloop()


# Secret text display

def show():
    print('Your ID is %s'% e1.get())
    print('Your password is %s'% e2.get())
root = Tk()

Label(root,text='ID:').grid(row=0,column=0)
Label(root,text='password:').grid(row=1,column=0)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(root,textvariable=v1)
e2 = Entry(root,textvariable=v2,show='*')
e1.grid(row=0,column=1,padx=5,pady=5)
e2.grid(row=1,column=1,padx=5,pady=5)

Button(root,text='Confirm',width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(root, text='Exit', width=10, command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)

mainloop()