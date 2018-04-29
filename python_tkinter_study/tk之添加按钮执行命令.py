# conda_python3_code

import tkinter as tk

class APP:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT,padx=100,pady=100) # set the position of frame

        self.hi_here = tk.Button(frame,text='hi',fg='blue',command=self.say_hi)
        self.hi_here.pack()# set the position of frame

        self.exit = tk.Button(frame,text='exit',fg='blue',command=exit)
        self.exit.pack()# set the position of frame

    def say_hi(self):
        print('Hello world')
root = tk.Tk()
app = APP(root)

root.mainloop()