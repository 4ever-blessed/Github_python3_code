# conda_python3_code

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

def test(content):
    return content.isdigit()

def calc():
    if not (v1.get() and v2.get()):
        v4.set(str('The input can not be EMPTY !').ljust(50))
    elif operator_chosen.current() == 0:
        result = int(v1.get()) + int(v2.get())
        v3.set(str(result))
        v4.set(str('Calc successfully !').ljust(50))
    elif operator_chosen.current() == 1:
        result = int(v1.get()) - int(v2.get())
        v3.set(str(result))
        v4.set(str('Calc successfully !').ljust(50))
    elif operator_chosen.current() == 2:
        result = int(v1.get()) * int(v2.get())
        v3.set(str(result))
        v4.set(str('Calc successfully !').ljust(50))
    elif (operator_chosen.current() == 3) and (int(v2.get())):
        result = int(v1.get()) / int(v2.get())
        v3.set(str(result))
        v4.set(str('Calc successfully !').ljust(50))
    elif operator_chosen.current() == 4:
        result = pow(int(v1.get()),int(v2.get()))
        v3.set(str(result))
    else:
        v4.set(str('The dividend can\'t be ZERO ! ').ljust(50))

def reset():
    v1.set(str(''))
    v2.set(str(''))
    v3.set(str(''))
    v4.set(str('Reset successfully !').ljust(50))

root = Tk()

root.title('easy_calculator')
frame = Frame(root)
frame.pack(padx=10,pady=10)
frame.columnconfigure(0, minsize=10)
frame.rowconfigure(0,minsize=50)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v4.set(str('ALL RIGHTS RESERVED.').ljust(50))

test_command = root.register(test)

# validate='key' means when user put down a key, the test command will be called.
# state='readonly' means user can not change the value of the entry.
e1 = Entry(frame,textvariable=v1,validate='key',validatecommand=(test_command,'%P')).grid(row=0,column=0)
e2 = Entry(frame,textvariable=v2,validate='key',validatecommand=(test_command,'%P')).grid(row=0,column=2)
e3 = Entry(frame,textvariable=v3,state='readonly').grid(row=0,column=4)

operator = StringVar()
operator_chosen = ttk.Combobox(frame, width=5, textvariable=operator)
operator_chosen['values'] = ('+','-','*','/','^')
operator_chosen.grid(row=0,column=1)
operator_chosen.current(0)

Label(frame,text='=').grid(row=0,column=3)
Label(frame,textvariable=v4).grid(row=3,column=0,columnspan=2)

img = Image.open('calc.jpg')  # open and decode image
photo = ImageTk.PhotoImage(img)
imgLabel = Label(frame,image=photo).grid(row=0, column=5, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

Button(frame,text='Calculate',width=10,command=calc).grid(row=1,column=1,sticky=(W,E,N,S),pady=5)
Button(frame,text='Reset',width=10,command=reset).grid(row=1,column=3,sticky=(W,E,N,S),pady=5)

mainloop()