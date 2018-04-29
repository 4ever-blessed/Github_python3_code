# conda_python3_code

from tkinter import *

def callback_slide(event):
    print ("Current position" + str(event.x) + "," + str(event.y))
def callback_mouse(event):
    print ("Click position is : " + str(event.x) + "," + str(event.y))
def callback_keyboard(event):
    print ("Key pressed is : ",event.keysym) #event.char
    
root = Tk()

frame = Frame(root,width=200,height=200)
frame.bind("<Button-1>",callback_mouse)
frame.bind("<KeyPress>",callback_keyboard)
frame.bind("<Motion>",callback_slide)
frame.focus_set()
frame.pack()

mainloop()