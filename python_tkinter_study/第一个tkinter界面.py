# conda_python3_code

import tkinter as tk

app = tk.Tk()
app.title('MY FIRST TK GUI DEMO')

theLabel = tk.Label(app,text='This is tkinter gui ! ')
theLabel.pack() # adjust the size of windows

app.mainloop()