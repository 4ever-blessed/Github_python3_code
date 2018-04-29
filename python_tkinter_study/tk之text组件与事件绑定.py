# conda_python3_code

from tkinter import *
import webbrowser

def show_arrow_cursor(event):
    text.config(cursor='arrow')
def show_xtrem_cursor(event):
    text.config(cursor='xterm')
def click(event):
    webbrowser.open('https://weibo.com/u/5018739340')

root = Tk()


text = Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,'Chingchi__All right reserved')

text.tag_add('link','1.0','1.8')
text.tag_config('link',foreground='blue',underline=True)
# bind the event
text.tag_bind('link','<Enter>',show_arrow_cursor)
text.tag_bind('link','<Leave>',show_xtrem_cursor)
text.tag_bind('link','<Button-1>',click)

mainloop()