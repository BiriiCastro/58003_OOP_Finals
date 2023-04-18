from tkinter import *

windows = Tk()
text = StringVar()
text.set("This is where I type my text")
ent = Entry(textvariable=text, width=25, bd=1)
ent.place(x=160, y=100, height=50)

windows.geometry("480x320+20+20")
windows.title("Text Field")
windows.mainloop()