# conda_python3_code

from tkinter import filedialog
from tkinter import *

root = Tk()

def callback():
    fileName = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GIF",".gif"),("JPG",".jpg"),("Python",".py")])    # defaultextension=".py"
    print(fileName)

Button(root,text="打开文件",command=callback).pack()

mainloop()