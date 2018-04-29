# conda_python3_code

from tkinter import *

root = Tk()

canvas = Canvas(root,width=200,height=100,background='white')
canvas.pack()

line1 = canvas.create_line(0,50,200,50,fill='red')
line2 = canvas.create_line(100,0,100,100,fill='red',dash=(4,4))
rect1 = canvas.create_rectangle(50,25,150,75,fill='blue')
text1 = canvas.create_text(100,50,text='Chingchi')

# move the object
canvas.coords(line1,0,25,200,25)
# config the object
canvas.itemconfig(rect1,fill='green')
# delete the object
#canvas.delete(line2)

Button(root,text='delete all',command=(lambda x=ALL:canvas.delete(x))).pack()

mainloop()