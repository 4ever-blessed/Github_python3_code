# conda_python3_code

from tkinter import *
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

def test():
    if e1.get() == 'kkk' or e1.get() == 'jcjc':
        print('Your name has been registered ! ')
        e1.delete(0,END)
        return True
    else:
        # print('Cons ! You can use this name ! ')
        return False
def test_2():
    if e1.get() == 'Jiang' or e1.get() == 'Fucker':
        print('The name is illegal ! ')
        e1.delete(0,END)
        return False
    else:
        print('Cons ! You can use this name ! ')
        return True
def show():
    print('Cons ! Your count is taking effect ! ')
    print('Your ID is %s'% e1.get())
    print('Your password is %s'% e2.get())

root = Tk()

Label(root,text='ID:').grid(row=0,column=0)
Label(root,text='password:').grid(row=1,column=0)

v1 = StringVar()
v2 = StringVar()

# When the validatecommand returns Faluse, the invalidcommand task will be called.
e1 = Entry(root,textvariable=v1,validate='focusout',validatecommand=test,invalidcommand=test_2)
e2 = Entry(root,textvariable=v2,show='*')
e1.grid(row=0,column=1,padx=5,pady=5)
e2.grid(row=1,column=1,padx=5,pady=5)

Button(root,text='Confirm',width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(root, text='Exit', width=10, command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)

mainloop()