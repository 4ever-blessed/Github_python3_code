# conda_python3_code

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# PIL is used for decode the JPG PNG format

master = Tk()
# four mode = SINGLE,BROWSE,MULTIPLE,EXTENDED
# height means the number of rows
frame1 = Frame(master)
frame2 = Frame(master)
frame1.pack(padx=10,pady=10,side=LEFT)
frame2.pack(padx=10,pady=10,side=RIGHT)

list_bottom = Listbox(frame1,selectmode=SINGLE,height=10)
list_bottom.pack()
del_button = Button(frame1,text='Destory the city \n'
                                '(Test the delete func)',
                    command=lambda x=list_bottom:x.delete(ACTIVE),fg='blue')
del_button.pack()

sb = Scrollbar(frame2)
sb.pack(side=RIGHT,fill=Y)
list_number = Listbox(frame2,selectmode=MULTIPLE,height=15,yscrollcommand=sb.set)
list_number.pack(side=LEFT,fill=BOTH)
sb.config(command=list_number.yview)

# first method
# list_bottom.insert(0,'Beijing')
# list_bottom.insert(1,'Shanghai')
# list_bottom.insert(2,'Guangzhou')
# list_bottom.insert(3,'Shenzhen')

# second method
# END means we put the item in the final position
for item in ['Beijing','Shanghai','Guangzhou','Shenzhen']:
    list_bottom.insert(END,item)


for item in range(130):
    list_number.insert(END,'Lv.'+str(item))

# delete method
# delete all
# list_bottom.delete(0,END)
# delete first choice
# list_bottom.delete(0)


mainloop()